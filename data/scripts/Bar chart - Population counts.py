import pandas as pd

#Fetch pop data
pop = pd.read_csv("https://ourworldindata.org/grapher/population.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})

# List of entities that are not countries, to filter out
non_country_entities = [
    "Africa (UN)",
    "Africa",
    "Americas (UN)",
    "Antarctica",
    "Asia",
    "Asia (UN)",
    "Asia (excl. China and India)",
    "Europe",
    "Europe (UN)",
    "Europe (excl. EU-27)",
    "Europe (excl. EU-28)",
    "Europe (excl. Russia)",
    "European Union (27)",
    "European Union (28)",
    "High-income countries",
    "Upper-middle-income countries",
    "International aviation",
    "International shipping",
    "Latin America and the Caribbean (UN)",
    "Low-income countries",
    "Lower-middle-income countries",
    "Northern America (UN)",
    "North America",
    "North America (excl. USA)",
    "Oceania",
    "Ryukyu Islands (GCP)",
    "Kuwaiti Oil Fires (GCP)",
    "South America",
    "South America (excl. Brazil)",
    "World"
]

# Filter only latest data, and exclude non countries
pop_cleaned = pop.loc[ (pop['Year'] == 2021) & (~pop['Entity'].isin(non_country_entities) ) & (pop['Entity'].notna()) ].copy()
# Sort by population
pop_cleaned.sort_values('population_historical', ascending=False, inplace=True)
# drop irrelevant columns
pop_cleaned.drop(columns=['Code','Year'], inplace=True)
# rename columns
pop_cleaned.rename(columns={'Entity':'Country','population_historical':'Population 2021'}, inplace=True)
# export only top 8 values
pop_cleaned.head(8).to_csv('./data/output/Bar chart - Population counts.csv', index=False)