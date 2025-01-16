import pandas as pd

# Fetch the data.
co2 = pd.read_csv("https://ourworldindata.org/grapher/co2-emissions-by-fuel-line.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})

# Filter for global data each decade from 1870 onward
co2_cleaned = co2[ (co2['Entity']=='World') & (co2['Year'] > 1800) & (co2['Year'] % 10 == 0) ].copy()

# Create other column
co2_cleaned['Cement, Flaring & Other Industry'] = co2_cleaned[['emissions_from_cement','emissions_from_flaring','emissions_from_other_industry']].sum(axis=1)

# Drop columns
co2_cleaned.drop(columns=['Entity','Code','emissions_from_cement','emissions_from_other_industry','emissions_from_flaring'], inplace=True)

# Relabel emissions columns
co2_cleaned.rename(columns={'emissions_from_oil' :'Oil','emissions_from_coal':'Coal','emissions_from_gas':'Gas'}, inplace=True)

# Create csv and sort by year
co2_cleaned.sort_values('Year').to_csv('./data/output/Line chart - CO2 emissions.csv', index=False)