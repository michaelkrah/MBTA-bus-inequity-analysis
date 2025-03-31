import pandas as pd
from datetime import datetime, timedelta, timedelta

def compute_trip_delays(input_csv, output_csv):
    # Read the CSV file
    df = (pd.read_csv(input_csv, low_memory=False))
    
    # Clean up column names by stripping whitespace
    df.columns = df.columns.str.strip()
    
    # Required columns:
    required_cols = ['service_date', 'route_id', 'direction_id', 'half_trip_id',
                     'time_point_order', 'scheduled', 'actual']
    for col in required_cols:
        if col not in df.columns:
            print(f"Error: Missing required column '{col}'. Found columns: {df.columns.tolist()}")
            return
    
    # Create a unique trip identifier
    df['trip_id'] = (df['service_date'].astype(str).str.strip() + "_" +
                     df['route_id'].astype(str).str.strip() + "_" +
                     df['direction_id'].astype(str).str.strip() + "_" +
                     df['half_trip_id'].astype(str).str.strip())
    
    # Ensure time_point_order is numeric.
    df['time_point_order'] = pd.to_numeric(df['time_point_order'], errors='coerce')
    
    # Parse scheduled and actual times into datetime objects.
    df['scheduled_dt'] = pd.to_datetime(df['scheduled'].str.strip(), utc=True, errors='coerce')
    df['actual_dt'] = pd.to_datetime(df['actual'].str.strip(), utc=True, errors='coerce')
    
    # Create a new df of trip_ids and delays
    results = df[['trip_id', 'scheduled_dt', 'actual_dt']]
    # Get the delay (currently NOT in seconds)
    results['delay_seconds'] = (results['actual_dt'] - results['scheduled_dt'])

    # Adjust for a likely day rollover only if scheduled time is late and actual time is very early
    # If sched.hour >= 23 and act.hour < 3, assume arrival is next day
    results.loc[(results['scheduled_dt'].dt.hour >= 23) & (results['actual_dt'].dt.hour < 3)]['delay_seconds'] += timedelta(days=1)

    # Convert to seconds
    results['delay_seconds'] = results['delay_seconds'].dt.total_seconds()

    # Create a DataFrame with the results and write to CSV file - make sure what we have isnt empty
    if not results.empty:
        results.to_csv(output_csv, index=False)
        print("Trip delays saved to:", output_csv)
    else:
        print("No valid trips found.")

if __name__ == "__main__":
    input_csv = "./MBTA_Bus_Ridership_by_Trip_Season_Route_Line_and_Stop/MBTA-Bus-Arrival-Departure-Times_2024-07.csv"  # Update as needed.
    output_csv = "trip_delays.csv"
    compute_trip_delays(input_csv, output_csv)
