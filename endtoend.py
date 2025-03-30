import pandas as pd
from datetime import datetime, timedelta

def compute_end_to_end_times(input_csv, output_csv):
    # First, try to read the CSV using tab as delimiter.
    df = pd.read_csv(input_csv, delimiter='\t', low_memory=False)
    
    # Check if the header was read as a single column.
    if len(df.columns) == 1:
        # The header appears as a single string; split it manually.
        # First, read the entire file as lines.
        with open(input_csv, 'r') as f:
            lines = f.readlines()
        # Assume the first line is the header.
        header = lines[0].strip().split(',')
        # The rest of the lines are data; join them into one string and then split each line.
        data = [line.strip().split(',') for line in lines[1:]]
        # Create a new DataFrame using the manually split data.
        df = pd.DataFrame(data, columns=header)
    
    # Strip whitespace from column names.
    df.columns = df.columns.str.strip()
    
    # Check that the required columns exist.
    required = ['service_date', 'route_id', 'direction_id', 'half_trip_id', 'time_point_order', 'scheduled']
    missing = [col for col in required if col not in df.columns]
    if missing:
        print("Error: Missing expected columns:", missing)
        print("Found columns:", df.columns.tolist())
        return

    # Create a unique trip identifier by concatenating service_date, route_id, direction_id, and half_trip_id.
    df['trip_id'] = (df['service_date'].astype(str).str.strip() + "_" +
                     df['route_id'].astype(str).str.strip() + "_" +
                     df['direction_id'].astype(str).str.strip() + "_" +
                     df['half_trip_id'].astype(str).str.strip())
    
    # Parse the 'scheduled' column into datetime objects.
    # Assume the scheduled times are in ISO 8601 format, e.g. "1900-01-01T10:06:00Z".
    df['scheduled_dt'] = pd.to_datetime(df['scheduled'].str.strip(), utc=True)
    
    results = []
    
    # Group by the unique trip identifier.
    for trip_id, group in df.groupby('trip_id'):
        # Sort by 'time_point_order' (if numeric, convert if necessary).
        group_sorted = group.sort_values(by='time_point_order')
        
        first_stop = group_sorted.iloc[0]
        last_stop = group_sorted.iloc[-1]
        
        start_time = first_stop['scheduled_dt']
        end_time = last_stop['scheduled_dt']
        
        # Handle day rollover: if the end time is earlier than the start time, assume arrival on the next day.
        if end_time < start_time:
            end_time += timedelta(days=1)
        
        duration_seconds = (end_time - start_time).total_seconds()
        
        results.append({
            'trip_id': trip_id,
            'end_to_end_seconds': duration_seconds
        })
    
    if results:
        results_df = pd.DataFrame(results)
        results_df.to_csv(output_csv, index=False)
        print("End-to-end times saved to:", output_csv)
    else:
        print("No valid trips found in the input CSV.")

if __name__ == "__main__":
    input_csv = "MBTA-Bus-Arrival-Departure-Times_2024-07.csv"
    output_csv = "end_to_end_times.csv"
    compute_end_to_end_times(input_csv, output_csv)
