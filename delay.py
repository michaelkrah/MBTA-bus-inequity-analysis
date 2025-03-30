import pandas as pd
from datetime import datetime, timedelta

def compute_trip_delays(input_csv, output_csv):
    # Read the CSV file (assumed comma-delimited)
    df = pd.read_csv(input_csv, low_memory=False)
    
    # Clean up column names by stripping whitespace
    df.columns = df.columns.str.strip()
    
    # Required columns for this computation:
    required_cols = ['service_date', 'route_id', 'direction_id', 'half_trip_id',
                     'time_point_order', 'scheduled', 'actual']
    for col in required_cols:
        if col not in df.columns:
            print(f"Error: Missing required column '{col}'. Found columns: {df.columns.tolist()}")
            return
    
    # Create a unique trip identifier by concatenating service_date, route_id, direction_id, and half_trip_id.
    df['trip_id'] = (df['service_date'].astype(str).str.strip() + "_" +
                     df['route_id'].astype(str).str.strip() + "_" +
                     df['direction_id'].astype(str).str.strip() + "_" +
                     df['half_trip_id'].astype(str).str.strip())
    
    # Ensure time_point_order is numeric.
    df['time_point_order'] = pd.to_numeric(df['time_point_order'], errors='coerce')
    
    # Parse scheduled and actual times into datetime objects.
    # These times are in ISO 8601 format, e.g. "1900-01-01T10:06:00Z".
    df['scheduled_dt'] = pd.to_datetime(df['scheduled'].str.strip(), utc=True, errors='coerce')
    df['actual_dt'] = pd.to_datetime(df['actual'].str.strip(), utc=True, errors='coerce')
    
    results = []
    
    # Group by trip_id
    for trip_id, group in df.groupby('trip_id'):
        # Sort the rows by time_point_order to ensure correct ordering of stops.
        group_sorted = group.sort_values(by='time_point_order')
        
        # For each trip, take the first row as the start and the last row as the end.
        start_row = group_sorted.iloc[0]
        end_row   = group_sorted.iloc[-1]
        
        sched = start_row['scheduled_dt']
        act   = end_row['actual_dt']
        
        # If either time is invalid, skip this trip.
        if pd.isnull(sched) or pd.isnull(act):
            continue
        
        # Compute the raw difference in seconds.
        raw_diff = (act - sched).total_seconds()
        
        # Adjust for a likely day rollover only if scheduled time is late and actual time is very early.
        # For example, if sched.hour >= 23 and act.hour < 3, assume arrival is next day.
        if sched.hour >= 23 and act.hour < 3:
            act_adjusted = act + timedelta(days=1)
            delay = (act_adjusted - sched).total_seconds()
        else:
            # Otherwise, use the raw difference, so an early arrival yields a negative delay.
            delay = raw_diff
        
        results.append({
            'trip_id': trip_id,
            'delay_seconds': delay
        })
    
    # Create a DataFrame with the results and write to a CSV file.
    if results:
        results_df = pd.DataFrame(results)
        results_df.to_csv(output_csv, index=False)
        print("Trip delays saved to:", output_csv)
    else:
        print("No valid trips found.")

if __name__ == "__main__":
    input_csv = "MBTA-Bus-Arrival-Departure-Times_2024-07.csv"  # Update as needed.
    output_csv = "trip_delays.csv"
    compute_trip_delays(input_csv, output_csv)
