import pandas as pd
from datetime import datetime, timedelta, timedelta
import sys

## Computes the difference between actual and scheuled arrival times per STOP, not trip.

def compute_trip_delays(input_csv, output_csv):
    # Read the CSV file
    df = (pd.read_csv(input_csv, low_memory=False))
    
    # Clean up column names by stripping whitespace
    df.columns = df.columns.str.strip()
    
    print(df.columns)

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

    # Convert to seconds
    results['delay_seconds'] = results['delay_seconds'].dt.total_seconds()

    # Create a DataFrame with the results and write to CSV file - make sure what we have isnt empty
    if not results.empty:
        results.to_csv(output_csv, index=False)
        print("Trip delays saved to:", output_csv)
    else:
        print("No valid trips found.")

if __name__ == "__main__":
    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    compute_trip_delays(input_csv, output_csv)
