# Boston Bus Equity

Spark Project - Public transport plays an important role in the quality of life for residents in Massachusetts and Boston in terms of economic development, the environment, and equity. The goal of this project is to better understand the impact of bus performance on Boston residents by using MBTA bus data to examine service performance trends by geography. More information on this specific project from Spark can be found [here](https://docs.google.com/document/d/1BDWIXxLIoyoAc7ZoDu54bQZFiHViBrydTfgQigjtaNY/edit?tab=t.0).

### Final Report Video Link:

[Youtube Presentation Link](https://youtu.be/62y40h25OEA)


### Local setup and testing:

We have included a requirements.txt file with necessary dependencies. Sample csv files have been generated and added to the datasets folder. These mimic the full datasets downloadable below, but folders and files have had the suffic _Sample added. This will need to be included in notebook files for local testing.   

### Datasets:

We  used the following datasets from the MBTA site:

- [Ridership data from 2018-2024](https://mbta-massdot.opendata.arcgis.com/datasets/8daf4a33925a4df59183f860826d29ee/about)
- [Bus Stop Location and IDs](https://mbta-massdot.opendata.arcgis.com/datasets/24a97982b39f4febb504c9e6cb55879b_0/explore)
- [Arrival and Departure Times 2019-2024](https://mbta-massdot.opendata.arcgis.com/search?collection=dataset&q=mbta%20bus%20arrival%20departure%20time)
- [2023 Passenger Wide Survey Data](https://mbta-massdot.opendata.arcgis.com/datasets/MassDOT::mbta-2023-system-wide-passenger-survey-data/about)


## Overview & Questions Addressed:

The Spark page includes a list of base questions to address. Each question has an associated notebook with analysis, details on specific topics are  below.  

### Ridership Data Processing and Modeling:
*What is the ridership per bus route? How has this changed from pre pandemic time to post pandemic time?*

Pre and post covid ridership was calculated using available monthly ridership data for the entire MBTA bus system and for available bus routes. Pre-covid pandemic data was considered as all data prior to 2019, and post-covid data as averages from 2022 2023, and 2024. Data from 2020 and 2021 was considered to be during covid and was not used, as this significantly impacted ridership. 

![Comparison of Ridership for all MBTA Routes](assets/bus_covid_ridership.png)
*Comparison of Ridership for all MBTA Routes*

We found that ridership has dropped across the MBTA bus system following COVID. Today, fewer people use the buses than 6 years ago. This is likely heavily influenced by the pandemic, as people may have begun to work from home or invest in alternative forms in transport. Following the end of the pandemic it appears that levels still have not returned to prepandemic levels. 


### End to End Data Processing and Modeling:
*What are the end-to-end travel times for each bus route in the city?*

The data, grouped by routes, will have an additional aggregate feature that contains the time in seconds between the arrival at the first stop and the arrival at the final stop. The intention of this feature is to reflect possible route efficiency changes over time, such as comparing pre and post-pandemic route duration times, along with the relative efficiency within areas of varying socioeconomic demographics. The motivation behind using route duration lies in its ability to contextualize route efficiency; it can be combined with other features like the number of stops to track per-stop efficiency, along with the accessibility and convenience of reaching certain areas of the city from areas of demographical interest.

![Average End to End time for Each Bus Route](assets/end_to_end_graph.png)
*Average end to end time for each bus route in the MBTA. The graph is colored orange for outbound buses and blue for inbound buses.*

### Wait Time Data Processing and Modeling:
*On average, how long does an individual have to wait for a bus (on time vs. delayed)?*

Wait times between buses can be calculated using headways data. Headways measure the scheduled and actual time between buses at specific stops. [Key routes](https://en.wikipedia.org/wiki/MBTA_key_bus_routes#) are routes with strict headway goals that they are expected to maintain during rush periods. We plotted scheduled and expected headways to understand how delays impacted wait times for bus riders. 

![Wait Times for Key Routes](assets/headway_average.png)
*Average scheduled vs actual headway by route on weekdays for 2024 season. Peak weekday times at 7:00am - 9:30am and 4:00pm - 6:30pm*


### Delay Data Processing and Modeling:
*What is the average delay time of all routes across the entire city?*
*What is the average delay time of the target bus routes (22, 29, 15, 45, 28, 44, 42, 17, 23, 31, 26, 111, 24, 33, 14 - from Livable Streets report)?*

Delays for individual bus trips was calculated by subtracting the actual arrival time from the scheduled arrival time in the arrival and departure dataset. This was then grouped by route and stop to find average and maximum delay times for all routes and stops. We were also able to look at other delay factors, such as percentage of buses more than 5 minutes late, as well as analyze the change in delays over time. We associated these results with available geospatial data for bus stop and route locations to cluster stops and visually analyze locational disparities in ArcGIS.

![Average Route Delay](assets/average_route_delay.png)
*Average delay for each route in the MBTA. Routes highlighted by the Livable Streets Report are highlighted in red.*

Looking across the MBTA, we found that delays were common. Buses frequently run late, are held up in traffic, or are cancelled. Notably, buses highlighted in the Liveable Streets Report face some of the worse average delays. These are bus routes that primarily serve vulnerable communities. 


### Route Level Service Disparities:
*Are there disparities in the service levels of different routes (which lines are late more often than others)?*
*Are there differences in the characteristics of the people most impacted*

For route levels service disparities, we compared ridership to headway, a measure of time between buses. This can give insight into the over or undercrowding of specifc bus routes, and shows what routes may need more resources. We also looked at routes with high delays and lowered ridership, to see if there was a correlation between delays and ridership. 

Using the 2024 survey, we have created graph breakdowns of different demographics (income, race, trip purpose, age, gender, and English-speaking).
Below are the graphs:

![Income](assets/income_breakdown.png)
*Breakdown of MBTA riders and their most frequent mode of transportation categorized via income.*

![Race](assets/race_breakdown.png)
*Breakdown of MBTA riders and their most frequent mode of transportation categorized via race.*

![Other Demographics](assets/other_demographics_breakdown.png)
*Breakdown of MBTA riders and their most frequent mode of transportation categorized via age, gender, and English-speaking ability.*

![Trip Purpose and Frequency](assets/trip_purpose_breakdown.png)
*Breakdown of MBTA riders and their most frequent mode of transportation categorized via trip purpose and frequency.*


### Changes over time (2018-2024):
*Can we chart changes over time?*

To understand how the bus system has changed over time, we first examined levels of ridership between 2018 and 2024. This gave a broad picture into how the MBTA has changed. We also plotted the change in delays between 2018 and 2024. This let us understand what routes may have improved and what routes may need attention.

![Change in average delay](assets/percent_change_in_avg_delay_2018_to_2024.png)
*Percent change in delay for routes over time. Routes highlighted by the Livable Streets Report are highlighted in red. Key routes are highlighted in green.*

Looking at changes over time, we found that most routes have had an increase in average delay since 2018. We also found that the percentage of buses more than 5 minutes late has increased for most routes, shown in our notebooks. Notably, routes highlighted by the Liveable Streets Report have seen significant increases in average delay since 2018. These routes primarily run through underserved communities and have previously been highlighted as needing improvements. However, this data only goes until 2024. The MBTA has released policy plans, available [here](https://www.mbta.com/projects/bus-network-redesign), that suggest changes for bus modernization beginning in 2025.  

### Results and Recommendations:

<img src="assets/boston_all_stations.png" alt="all_boston_stations" width="500">*All Boston Bus Stops*

<img src="assets/boston_stops_with_highest_average_delay.png" alt="boston_stops_with_highest_average_delay" width="500">*10% of Bus Stops with Highest Recorded Absolute Average Delay*

![average_route_delay](assets/average_route_delay.png)
*Average Absolute Route Delay, Stops Identified By the Livable Streets Report Are Highlighted*

Initial results show higher than average levels of delays among the bus routes first identified as underserved by the livable street reports in 2019 [here](https://d3n8a8pro7vhmx.cloudfront.net/livablestreetsalliance/pages/6582/attachments/original/1569205099/lsa-better-buses-2019-v9-20sep19.pdf?1569205099). We hope to further analyze this trend to understand how these disparities have changed over time, especially in the context of lower bus usage post-covid. We plan to analyze locational clusters of stops or routes that may be underserved to identify if there are any correlations between these disparities and groups impacted. 


### Adjacent Findings:




### Future Work:

