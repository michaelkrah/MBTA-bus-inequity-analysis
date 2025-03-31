# Boston Bus Equity 

Spark Project - Public transport plays an important role in the quality of life for residents in Massachusetts and Boston in terms of economic development, the environment, and equity. The goal of this project is to better understand the impact of bus performance on Boston residents by using MBTA bus data to examine service performance trends by geography. More information on this specific project from Spark can be found [here](https://docs.google.com/document/d/1BDWIXxLIoyoAc7ZoDu54bQZFiHViBrydTfgQigjtaNY/edit?tab=t.0).


# Midterm Report:

## Video Link: 

## Preliminary visualizations of data

## Detailed description of data processing done so far

## Detailed description of data modeling methods used so far

## Preliminary results.



# Initial Proposal:

## Goals:
This project includes a list of key questions that can be investigated. To better understand the impact of bus performance we plan to investigate as many as possible over the semester. These include: 
- Ridership Analysis: Determine ridership per bus route and assess changes over time, comparing pre- and post-pandemic periods.
- Travel Times: Evaluate end-to-end travel time and wait times for each bus route.
- Delay Metrics: Compute average delay times both citywide and for target routes identified in the Livable Streets report.
- Equity Assessment: Analyze if service disparities correlate with demographic characteristics such as race, ethnicity, income, or age.
- Trend Visualization: Create time series and geospatial visualizations to reveal performance trends and pinpoint areas for improvement.

## Data Collection:
This project includes several main datasets that we will use for the bulk of our analysis.  
Primary Datasets:
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
