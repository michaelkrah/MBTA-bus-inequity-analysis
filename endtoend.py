import pandas as pd
from datetime import datetime, timedelta
import sys

## Computes the duration of each full trip in seconds
# Takes two file paths as arguments - one for the dataset to be used, one for the resulting csv.

def compute_end_to_end_times(input_csv, output_csv):
    # Read CSV
    df = (pd.read_csv(input_csv, low_memory=False))
    
    # Strip whitespace from column names.
    df.columns = df.columns.str.strip()
    
    # Check that the required columns exist
    required = ['service_date', 'route_id', 'direction_id', 'half_trip_id', 'time_point_order', 'actual']
    missing = [col for col in required if col not in df.columns]
    if missing:
        print("Error: Missing expected columns:", missing)
        print("Found columns:", df.columns.tolist())
        return

    # Create a unique trip identifier
    df['trip_id'] = (df['service_date'].astype(str).str.strip() + "_" +
                     df['route_id'].astype(str).str.strip() + "_" +
                     df['direction_id'].astype(str).str.strip() + "_" +
                     df['half_trip_id'].astype(str).str.strip())
    
    # Convert the actual arrival times into date-time objects
    df['actual_dt'] = pd.to_datetime(df['actual'].str.strip(), utc=True)
    
    # Create the results df - aggregate the first and last arrival times into an entry for each trip - reset the index so we keep the id's.
    results = df.groupby('trip_id').agg(first_arrival=('actual_dt', 'min'), last_arrival=('actual_dt', 'max')).reset_index()
    # Add a duration column - in seconds
    results['duration_seconds'] = (results['last_arrival'] - results['first_arrival']).dt.total_seconds()
    # We only want the trip id, start and end times, and duration (in seconds)
    results = results[['trip_id', 'first_arrival', 'last_arrival', 'duration_seconds']]

    if not results.empty:
        results.to_csv(output_csv, index=False)
        print("End-to-end times saved to:", output_csv)
    else:
        print("No valid trips found in the input CSV.")

if __name__ == "__main__":
    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    compute_end_to_end_times(input_csv, output_csv)
