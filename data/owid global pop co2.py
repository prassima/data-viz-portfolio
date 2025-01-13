#ensure all libraries are installed: in terminal (mac) or command line (win), run the following `pip install -r requirements.txt`
#for this script, the libraries are: pandas requests
import pandas as pd

# Fetch the data.
co2 = pd.read_csv("https://ourworldindata.org/grapher/co2-emissions-by-fuel-line.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})
# Filter for global data from 1800
co2_cleaned = co2[ (co2['Entity']=='World') & (co2['Year'] > 1800) & (co2['Year'] % 10 == 0) ].copy()
# Create overall CO2 emissions column
co2_cleaned['Annual CO2 emissions'] = co2_cleaned[['emissions_from_oil','emissions_from_coal','emissions_from_cement','emissions_from_flaring','emissions_from_gas','emissions_from_other_industry']].sum(axis=1)

#Fetch pop data
pop = pd.read_csv("https://ourworldindata.org/grapher/population.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})
# Filter for global data from 1800
pop_cleaned = pop[ (pop['Entity']=='World') & (pop['Year'] > 1800) & (pop['Year'] % 10 == 0)].copy()

# Join dfs
global_cleaned = co2_cleaned.merge(pop_cleaned, on='Year', suffixes=('_co2', '_pop'))

# Calculate per capita CO2 emissions
global_cleaned['co2_per_capita'] = global_cleaned['Annual CO2 emissions'] / global_cleaned['population_historical']
# Drop unnecessary columns
global_cleaned.drop(columns=['Entity_co2','Entity_pop','Code_co2','Code_pop'], inplace = True)

# Create csv and sort by year
global_cleaned.sort_values('Year').to_csv('data/global_pop_co2.csv', index=False)