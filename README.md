# [Health Facilities in Ghana Dashboard](https://public.tableau.com/app/profile/osikanyi.essandoh/viz/HealthFacilitiesinGhana_16784497844140/HEALTHFACILITIESOVERVIEW)
This project visualizes the distribution of health facilities in Ghana by region, ownership, type, and population density. The data was obtained from the Ghana Open Data Initiative and Wikipedia, and was analyzed and visualized using Tableau.

## Data Sources
The following datasets were used for this project:

1. Health Facilities in Ghana: [health-facilities-gh](https://github.com/Osikanyi-The-Analyst/Health-Facilities-in-Ghana-Overview/blob/main/health-facilities-gh.csv) and [health-facility-tiers](https://github.com/Osikanyi-The-Analyst/Health-Facilities-in-Ghana-Overview/blob/main/health-facility-tiers.csv) from Kaggle.
2. [Regional Population in Ghana](https://github.com/Osikanyi-The-Analyst/Health-Facilities-in-Ghana-Overview/blob/main/regional_population.csv): web scrapped from Wikipedia.
3. [Regional Area in Ghana](https://github.com/Osikanyi-The-Analyst/Health-Facilities-in-Ghana-Overview/blob/main/Regional_Area.csv): web scrapped from Wikipedia.

## Web Scraping
To obtain the necessary population and area data for each region in Ghana, web scraping was employed. The population and area data were obtained from the Wikipedia pages on the List of Ghanaian regions by population and List of Ghanaian regions by area, respectively. The web scraping process was done using Python and the Beautiful Soup library. Here are the python codes used for the web scraping
1. [Regional_Area.py](https://github.com/Osikanyi-The-Analyst/Health-Facilities-in-Ghana-Overview/blob/main/Regional_Area.py)
2. [regional_population.py](https://github.com/Osikanyi-The-Analyst/Health-Facilities-in-Ghana-Overview/blob/main/regional_population.py)

## [Tableau Dashboard](https://public.tableau.com/app/profile/osikanyi.essandoh/viz/HealthFacilitiesinGhana_16784497844140/HEALTHFACILITIESOVERVIEW)
The Tableau dashboard includes the following visualizations:

1. Facilities by Region: displays the number of health facilities in each region of Ghana.
2. Facilities by Ownership: displays the distribution of health facilities by ownership type (public, private, or quasi-government).
3. Facilities Area Density: displays the density of health facilities per square kilometer for each region of Ghana.
4. Facilities Population Density: displays the density of health facilities per 10,000 people for each region of Ghana.
5. Facilities by Type: displays the distribution of health facilities by type (hospitals, clinics, health directorates, maternity homes, health centers, CHPS, RCH, directorates, and others).
6. Regional Key Indicators: shows key indicators such as the total number of facilities, and the count and percentage of each facility type.

## Repository Contents
The following files can be found in this repository:

1. [health-facilities-gh.csv](https://github.com/Osikanyi-The-Analyst/Health-Facilities-in-Ghana-Overview/blob/main/health-facilities-gh.csv): the original dataset obtained from Kaggle.
2. [health-facility-tiers.csv](https://github.com/Osikanyi-The-Analyst/Health-Facilities-in-Ghana-Overview/blob/main/health-facility-tiers.csv): the original dataset obtained from Kaggle.
3. [regional_population.csv](https://github.com/Osikanyi-The-Analyst/Health-Facilities-in-Ghana-Overview/blob/main/regional_population.csv): the cleaned dataset obtained from Wikipedia.
4. [regional_area.csv](https://github.com/Osikanyi-The-Analyst/Health-Facilities-in-Ghana-Overview/blob/main/Regional_Area.csv): the cleaned dataset obtained from Wikipedia.
5. Health Facilities in Ghana.twb: the Tableau workbook containing the visualizations.
6. README.md: this file.
7. [Regional_Area.py](https://github.com/Osikanyi-The-Analyst/Health-Facilities-in-Ghana-Overview/blob/main/Regional_Area.py): Python code for scrapping Regional Areas
8. [regional_population.py](https://github.com/Osikanyi-The-Analyst/Health-Facilities-in-Ghana-Overview/blob/main/regional_population.py): Python Code for scrapping Population of Regions.


## Usage
To interact with the [Tableau dashboard](https://public.tableau.com/app/profile/osikanyi.essandoh/viz/HealthFacilitiesinGhana_16784497844140/HEALTHFACILITIESOVERVIEW).

## Acknowledgments
Special thanks to the Ghana Open Data Initiative and Wikipedia for providing the data used in this project.
