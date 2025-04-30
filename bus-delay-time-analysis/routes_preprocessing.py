# Python file to standarize preprocessing of routes across different jupyter notebooks
import pandas as pd
import numpy as np

def preprocess_routes(routes_df: pd.DataFrame) -> pd.DataFrame:
  # Clean up data: Some bus lines are used as temporary shuttles, are the silver line, or aren't on the mbta page
  routes_df = routes_df[~routes_df['route_id'].str.startswith(('600', '700', 'rad', '743', "171", "194"))]

  routes_df['time_difference'] = pd.to_datetime(routes_df['actual']) - pd.to_datetime(routes_df['scheduled'])
  routes_df['delay_seconds'] = routes_df['time_difference'].dt.total_seconds()
  routes_df['delay_headway'] = routes_df['headway'] - routes_df['scheduled_headway']

  # Done to get rid of extreme outliers
  filtered_df = routes_df[(routes_df['delay_seconds'] >= -3600) & (routes_df['delay_seconds'] <= 3600)]
  positive_delays = filtered_df[filtered_df['delay_seconds'] > 0]
  avg_positive_delay_per_route = positive_delays.groupby('route_id')['delay_seconds'].mean().reset_index()
  return avg_positive_delay_per_route
