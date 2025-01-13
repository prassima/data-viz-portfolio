#ensure all libraries are installed: in terminal (mac) or command line (win), run the following `pip install -r requirements.txt`
#for this script, the libraries are: pandas requests
import pandas as pd

# Fetch the data.
co2 = pd.read_csv("https://ourworldindata.org/grapher/co2-emissions-by-fuel-line.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})
# Filter for global data from 1800
co2_cleaned = co2[ (co2['Year'] >= 1870) & (co2['Year'] % 10 == 0) ].copy()
# Create overall CO2 emissions column
co2_cleaned['Annual CO2 emissions'] = co2_cleaned[['emissions_from_oil','emissions_from_coal','emissions_from_cement','emissions_from_flaring','emissions_from_gas','emissions_from_other_industry']].sum(axis=1)

#Fetch pop data
pop = pd.read_csv("https://ourworldindata.org/grapher/population.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})
# Filter for global data from 1800
pop_cleaned = pop[ (pop['Year'] >= 1870) & (pop['Year'] % 10 == 0)].copy()

# List of entities that are not countries, to filter out
non_country_entities = [
    "Africa",
    "Antarctica",
    "Asia",
    "Asia (excl. China and India)",
    "Europe",
    "Europe (excl. EU-27)",
    "Europe (excl. EU-28)",
    "European Union (27)",
    "European Union (28)",
    "High-income countries",
    "Upper-middle-income countries",
    "International aviation",
    "International shipping",
    "Low-income countries",
    "Lower-middle-income countries",
    "North America",
    "North America (excl. USA)",
    "Oceania",
    "Ryukyu Islands (GCP)",
    "Kuwaiti Oil Fires (GCP)",
    "South America",
    "World"
]


# Get majority white countries
race_url = 'https://worldpopulationreview.com/country-rankings/caucasian-countries'
race = pd.read_html(race_url)
# We want 2nd table
race_table = race[1]
# Add column to identify racist countries, and drop continent
race_table['Caucasian']=True
race_table.drop(columns=['Continent'], axis=1, inplace=True)
race_table.rename(columns={'Country':'Entity'}, inplace=True)

# Join dfs
df = co2_cleaned.merge(pop_cleaned, on=['Year', 'Entity'], suffixes=('_co2', '_pop'), how='left')
# inner join on race table to only keep countries with race data
df = df.merge(race_table, on='Entity', how='left')
# exclude non country entities
df = df[~df['Entity'].isin(non_country_entities)]
df['Caucasian']=df['Caucasian'].fillna(False)
df['Caucasian']=df['Caucasian'].astype(bool)

# Calculate per capita CO2 emissions
df['co2_per_capita'] = df['Annual CO2 emissions'] / df['population_historical']

grouped_df = df.groupby(['Year', 'Caucasian']).agg(
    total_emissions=('Annual CO2 emissions', 'sum'),
    total_population=('population_historical', 'sum')
).reset_index()

# Calculate CO2 per capita
grouped_df['co2_per_capita'] = grouped_df['total_emissions'] / grouped_df['total_population']

# Optionally, drop intermediate columns if not needed
grouped_df = grouped_df.drop(columns=['total_emissions', 'total_population'])

pivoted_df = grouped_df.pivot(index='Year', columns='Caucasian', values='co2_per_capita').reset_index()

# Create csv and sort by year
df.sort_values(['Entity','Year']).to_csv('data/countries_trended_pop_co2.csv', index=False)
pivoted_df.sort_values('Year').to_csv('data/trended_race_pop_co2.csv', index=False)