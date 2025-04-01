# Boston Bus Equity

Spark Project - Public transport plays an important role in the quality of life for residents in Massachusetts and Boston in terms of economic development, the environment, and equity. The goal of this project is to better understand the impact of bus performance on Boston residents by using MBTA bus data to examine service performance trends by geography. More information on this specific project from Spark can be found [here](https://docs.google.com/document/d/1BDWIXxLIoyoAc7ZoDu54bQZFiHViBrydTfgQigjtaNY/edit?tab=t.0).

### Video Link:

[Youtube Presentation Link](https://youtu.be/62y40h25OEA)

### Datasets:

We have used the following datasets from the MBTA site:

- [Ridership data from 2018-2024](https://mbta-massdot.opendata.arcgis.com/datasets/8daf4a33925a4df59183f860826d29ee/about)
- [Bus Stop Location and IDs](https://mbta-massdot.opendata.arcgis.com/datasets/24a97982b39f4febb504c9e6cb55879b_0/explore)
- [Arrival and Departure Times 2019-2024](https://mbta-massdot.opendata.arcgis.com/search?collection=dataset&q=mbta%20bus%20arrival%20departure%20time)
- [2023 Passenger Wide Survey Data](https://mbta-massdot.opendata.arcgis.com/datasets/MassDOT::mbta-2023-system-wide-passenger-survey-data/about)

### Ridership Data Processing and Modeling:

Pre and post covid ridership was calculated using available monthly ridership data for the entire MBTA bus system and for available bus routes. Pre-covid data was considered as all data from 2019, and post-covid data as averages from 2022 and 2023, and 2024. Data from 2020 and 2021 was considered to be during covid and was not used.

![Comparison of Ridership for all MBTA Routes](assets/bus_covid_ridership.png)
*Comparison of Ridership for all MBTA Routes*


### End to End Data Processing and Modeling:

The data, grouped by routes, will have an additional aggregate feature that contains the time in seconds between the arrival at the first stop and the arrival at the final stop. The intention of this feature is to reflect possible route efficiency changes over time, such as comparing pre and post-pandemic route duration times, along with the relative efficiency within areas of varying socioeconomic demographics. The motivation behind using route duration lies in its ability to contextualize route efficiency; it can be combined with other features like the number of stops to track per-stop efficiency, along with the accessibility and convenience of reaching certain areas of the city from areas of demographical interest.

### Delay Data Processing and Modeling:

Delays for individual bus trips was calculated by subtracting the actual arrival time from the scheduled arrival time in the arrival and departure dataset. This was then grouped by route and stop to find average and maximum delay times for all routes and stops. We associated these results with available geospatial data for bus stop and route locations to cluster stops and visually analyze locational disparities in ArcGIS.

### Visualizations and Preliminary Results:

![all_boston_stations](assets/boston_all_stations.png)
*All Boston Bus Stops*

![boston_stops_with_highest_average_delay.png](assets/boston_stops_with_highest_average_delay.png)
*10% of Bus Stops with Highest Recorded Absolute Average Delay*

![average_route_delay](assets/average_route_delay.png)
*Average Absolute Route Delay, Stops Identified By the Livable Streets Report Are Highlighted*

Initial results show higher than average levels of delays among the bus routes first identified as underserved by the livable street reports in 2019 [here](https://d3n8a8pro7vhmx.cloudfront.net/livablestreetsalliance/pages/6582/attachments/original/1569205099/lsa-better-buses-2019-v9-20sep19.pdf?1569205099). We hope to further analyze this trend to understand how these disparities have changed over time, especially in the context of lower bus usage post-covid. We plan to analyze locational clusters of stops or routes that may be underserved to identify if there are any correlations between these disparities and groups impacted. 

# Initial Proposal:

## Goals:

This project includes a list of key questions that can be investigated. To better understand the impact of bus performance we plan to investigate as many as possible over the semester. These include:

- Ridership Analysis: Determine ridership per bus route and assess changes over time, comparing pre- and post-pandemic periods.
- Travel Times: Evaluate end-to-end travel time and wait times for each bus route.
- Delay Metrics: Compute average delay times both citywide and for target routes identified in the Livable Streets report.
- Equity Assessment: Analyze if service disparities correlate with demographic characteristics such as race, ethnicity, income, or age.
- Trend Visualization: Create time series and geospatial visualizations to reveal performance trends and pinpoint areas for improvement.

## Data Collection:

This project includes several main datasets that we will use for the bulk of our analysis.Primary Datasets:

- MBTA Bus Arrival/Departure Times (2018–2024) for reliability analysis. Available [here](https://mbta-massdot.opendata.arcgis.com/search?collection=dataset&q=mbta%20bus%20arrival%20departure%20time).
- Bus Ridership by Trip, Season, Route/Line, and Stop. Available [here](https://mbta-massdot.opendata.arcgis.com/datasets/eec03d901d2e470ebd5758c60d793e8e_0/explore).
- MBTA 2023 System-Wide Passenger Survey Data. Available [here](https://mbta-massdot.opendata.arcgis.com/datasets/faaf1295847e4673a03b40cef2c53df1_0/explore).

Supplementary Data:

- Rider Census interactive tool data.
- Demographic data from the 2020 Census for Boston and ACS transportation surveys.
- PATI Bus Stop Coordinates for geospatial mapping.
- Technical Documentation: Detailed data dictionaries and technical documentation are available to
  ensure proper data understanding and integration.

## Data Modelling:

- Standardization: Normalize datasets to consistent formats (date/time, route identifiers, etc.) and handle missing values.
- Integration: Merge disparate datasets (e.g., reliability and ridership data) using common identifiers.
- Validation: Verify the accuracy of data entries with reference to MBTA’s technical documentation and external reports.
  Feature Extraction
- Performance Metrics: Compute key metrics such as average travel times, wait times, and delay durations.
- Temporal Features: Extract time-based features (e.g., time-of-day, day-of-week, seasonality) for trend analysis.
- Spatial Features: Derive geospatial attributes from bus stop coordinates to map service levels by neighborhood.
- Demographic Linkages: Incorporate demographic features from census data to analyze equity in service distribution.

## Data visualization:

- Ridership Trends: Line charts comparing pre- and post-pandemic ridership by route.
- Travel & Wait Times: Box plots and histograms illustrating the distribution of travel and wait times.
- Delay Analysis: Bar charts showing average delay times citywide and for specific target routes.
- Geospatial Maps: Thematic maps displaying service levels and demographic overlays to highlight equity disparities.
- Time Series Maps: Animated visualizations to depict temporal changes in service performance.

## Testing:

- Data Split: Validate trends using historical data (2015–2017) versus the most recent MBTA data.
- Statistical Metrics: Monitor summary statistics (mean, median, variance) for key performance indicators.
- Visual Quality: Ensure visualizations are clear, informative, and accurately represent underlying data trends.
- Stakeholder Feedback: Gather input from the City of Boston Analytics Team and community partners to refine analyses and recommendations.
