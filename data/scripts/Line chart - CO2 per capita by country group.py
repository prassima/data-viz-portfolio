import pandas as pd

# Fetch the data.
co2 = pd.read_csv("https://ourworldindata.org/grapher/co2-emissions-by-fuel-line.csv?v=1&csvType=full&useColumnShortNames=true",
                  storage_options={'User-Agent': 'Our World In Data data fetch/1.0'})

# Filter for global data from 1870
co2_cleaned = co2.loc[
    (co2['Year'] >= 1870) & (co2['Year'] % 10 == 0)
    ].copy()

# Create overall CO2 emissions column
co2_cleaned['Annual CO2 emissions'] = co2_cleaned[
    ['emissions_from_oil', 'emissions_from_coal', 'emissions_from_cement',
     'emissions_from_flaring', 'emissions_from_gas', 'emissions_from_other_industry']
].sum(axis=1)

# Fetch pop data
pop = pd.read_csv("https://ourworldindata.org/grapher/population.csv?v=1&csvType=full&useColumnShortNames=true",
                  storage_options={'User-Agent': 'Our World In Data data fetch/1.0'})

# Filter for global data from 1870
pop_cleaned = pop.loc[
    (pop['Year'] >= 1870) & (pop['Year'] % 10 == 0)
    ].copy()

# List of entities that are not countries, to filter out
non_country_entities = [
    "Africa", "Antarctica", "Asia", "Asia (excl. China and India)", "Europe",
    "Europe (excl. EU-27)", "Europe (excl. EU-28)", "European Union (27)",
    "European Union (28)", "High-income countries", "Upper-middle-income countries",
    "International aviation", "International shipping", "Low-income countries",
    "Lower-middle-income countries", "North America", "North America (excl. USA)",
    "Oceania", "Ryukyu Islands (GCP)", "Kuwaiti Oil Fires (GCP)", "South America"
]

# Get majority white countries
race_url = 'https://worldpopulationreview.com/country-rankings/caucasian-countries'
race = pd.read_html(race_url)
# We want 2nd table
race_table = race[1].copy()

# Add column to identify racist countries, and drop continent
race_table['Classification'] = 'Majority white'
race_table.drop(columns=['Continent'], inplace=True)
race_table.rename(columns={'Country': 'Entity'}, inplace=True)

# Join dfs
df = co2_cleaned.merge(pop_cleaned, on=['Year', 'Entity'], suffixes=('_co2', '_pop'), how='left')
df = df.merge(race_table, on='Entity', how='left')

# Exclude non-country entities
df = df[~df['Entity'].isin(non_country_entities)].copy()

# Fill missing classifications and assign 'Global average' for 'World'
df['Classification'] = df['Classification'].fillna('Majority non-white')
df.loc[df['Entity'] == 'World', 'Classification'] = 'Global average'

# Calculate per capita CO2 emissions
df['co2_per_capita'] = df['Annual CO2 emissions'] / df['population_historical']

# Group and calculate total emissions and population by classification
grouped_df = df.groupby(['Year', 'Classification']).agg(
    total_emissions=('Annual CO2 emissions', 'sum'),
    total_population=('population_historical', 'sum')
).reset_index()

# Calculate CO2 per capita
grouped_df['co2_per_capita'] = grouped_df['total_emissions'] / grouped_df['total_population']

# Drop intermediate columns
grouped_df = grouped_df.drop(columns=['total_emissions', 'total_population'])

# Pivot the data
pivoted_df = grouped_df.pivot(index='Year', columns='Classification', values='co2_per_capita').reset_index()

# Create csv and sort by year
pivoted_df.sort_values('Year').to_csv('./data/output/Line chart - CO2 per capita by country group.csv', index=False)