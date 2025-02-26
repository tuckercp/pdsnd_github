
# Exploring US Bikeshare Data with Python

This project is part of the Udacity Programming for Data Science Nanodegree.  The purpose of this project is to use Python, specifically Pandas to explore bikesharing data for 3 major US cities during the first 6 months of 2017.

### Description
---
This project investigates bike sharing data for Chicago, New York and Washington D.C. The program aims to provide users with a complete, interactive experience using Python and Pandas. 
Users will select a city and then have the ability to apply various filters to the data, i.e. month, day, user type, gender and/or birth year. Various statistics will then be computed based on those filters, i.e. travel times, ride duration times, as well as other user info statistics.
Finally, users will have the option to view the raw data and/or reset the data to view a different city.

### Getting Started
---
To run this project, ensure you have the following installed:
* Python
* Pandas

### Files Used
---
* bikeshare.py
* bikeshareart.py
* chicago.csv
* new\_york\_city.csv
* washington.csv

### Usage
---
An example of the expected output is provided below:

Which US city data would you like to view? Chicago, New York or Washington **chicago**

You will be viewing Chicago Bikesharing data!

Would you like to filter the data by the month, day or both? Type 'other or none' to skip to other filters **both**

Please enter the month, followed by the day of the week, separated by a comma (ex. June, Sunday) **march, thursday**

Would you like to filter by user type, gender or birth year? Type Yes or No **yes**

Filter by user type? Type Subscriber, Customer or None **subscriber**

Filter by gender? Type Male, Female or None **female**

Filter by birth year? Please type the year (For no filter, type 0) **0**


#### Chicago Bikeshare Statistics

Filters applied: Month: March | Day: Thursday | User Type: Subscriber | Gender: Female | Birth Year: None

_Calcuating the most and least popular travel times..._
Most popular hour: 5PM (146) | Least popular hour: 2AM (1)

Processing request: 0.001756906509399414 seconds.

_Calcuating the most and least popular stations and trips..._
Most popular start station: Daley Center Plaza (15) | Least popular start station: Damen Ave & Foster Ave (1)
Most popular end station: Clinton St & Washington Blvd (16) | Least popular end station: Broadway & Ridge Ave (1)
Most popular trip: Ellis Ave & 55th St to Kimbark Ave & 53rd St (5)

Processing request: 0.0014090538024902344 seconds.

_Calcuating statistics on ride times in minutes..._
Total ride time (min.sec): 9478.4 | Average ride time (min.sec): 10.12 | Number of rides: 930
Longest ride (min.sec): 43.46 | Shortest ride (min.sec): 1.15

Processing request: 0.0004417896270751953 seconds.

_Calcuating statistics on user types and gender..._
Most common birth year: 1989 | Least common birth year: 1950
Average birth year: 1981 | Oldest birth year: 1998 | Youngest birth year: 1949

Processing request: 0.0005109310150146484 seconds.

There are 930 records in the DataFrame

Would you like to view raw data for Chicago? Type Yes or No **yes**

#### Chicago Bikeshare Data
  Unnamed: 0          Start Time            End Time  Duration in Seconds                   Start Station  ...  Gender Birth Year  Month Day of Week  Hour
26        385517 2017-03-23 09:38:27 2017-03-23 09:42:41                  254        Loomis St & Jackson Blvd  ...  Female     1985.0  March    Thursday   9AM
34        389463 2017-03-23 20:50:57 2017-03-23 20:57:19                  382             Ellis Ave & 55th St  ...  Female     1993.0  March    Thursday   8PM
650       351520 2017-03-16 20:22:23 2017-03-16 20:29:03                  400  Sheffield Ave & Wellington Ave  ...  Female     1979.0  March    Thursday   8PM
1157      326951 2017-03-09 17:02:12 2017-03-09 17:06:16                  244            Clinton St & Lake St  ...  Female     1956.0  March    Thursday   5PM
1648      384051 2017-03-23 07:00:19 2017-03-23 07:33:46                 2007    Marshfield Ave & Cortland St  ...  Female     1976.0  March    Thursday   7AM

5 rows x 13 columns

Would you like to view more raw data in Chicago? Type Yes or No **no**

Would you like to reset? Type Yes or No **no**

### Date Created
---
This project was created on 08/26/23. Edited on 08/28/23.

### Credits
---
bikeshareart.py credited to the ACSII Art Archive, specifically Gilo 94’ as initialed in the file; [https://www.asciiart.eu/sports-and-outdoors/cycling#google\_vignette][1]

[1]:	https://www.asciiart.eu/sports-and-outdoors/cycling#google_vignette