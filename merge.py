import pandas as pd

# List of CSV filenames to merge.
filenames = [
    "MBTA_Bus_Ridership_by_Trip_Season_Route_Line_and_Stop_Fall_2016.csv",
    "MBTA_Bus_Ridership_by_Trip_Season_Route_Line_and_Stop_Fall_2017.csv",
    "MBTA_Bus_Ridership_by_Trip_Season_Route_Line_and_Stop_Fall_2018.csv",
    "MBTA_Bus_Ridership_by_Trip_Season_Route_Line_and_Stop_Fall_2019.csv",
    "MBTA_Bus_Ridership_by_Trip_Season_Route_Line_and_Stop_Fall_2020.csv",
    "MBTA_Bus_Ridership_by_Trip_Season_Route_Line_and_Stop_Fall_2021.csv",
    "MBTA_Bus_Ridership_by_Trip_Season_Route_Line_and_Stop_Fall_2022.csv",
    "MBTA_Bus_Ridership_by_Trip_Season_Route_Line_and_Stop_Fall_2023.csv",
    "MBTA_Bus_Ridership_by_Trip_Season_Route_Line_and_Stop_Fall_2024.csv",
    "MBTA_Bus_Ridership_by_Trip_Season_Route_Line_and_Stop_Spring_2024.csv"
]

# Read each CSV file into a DataFrame with low_memory=False to avoid dtype warnings.
dfs = [pd.read_csv(filename, low_memory=False) for filename in filenames]

# Concatenate all DataFrames into one.
merged_df = pd.concat(dfs, ignore_index=True)

# Write the merged DataFrame to a new CSV file.
merged_df.to_csv("MBTA_Bus_Ridership_Merged.csv", index=False)

print("Merged CSV file created: MBTA_Bus_Ridership_Merged.csv")
