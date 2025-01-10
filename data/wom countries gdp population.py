##pip requirements: pandas pycountry pycountry-convert
import pandas as pd
import pycountry
import pycountry_convert as pc

# URL of the webpage containing the table
url = 'https://www.worldometers.info/gdp/gdp-by-country/'
tables = pd.read_html(url)

# The first/only table is the one we want
gdp_table = tables[0]

# Manual mapping dictionary for strings that pycountry doesn't recognise
manual_continent_mapping = {
    'Russia': 'Europe',
    'Turkey': 'Europe',
    'Czech Republic (Czechia)': 'Europe',
    'DR Congo': 'Africa',
    'State of Palestine': 'Asia',
    'Brunei': 'Asia',
    'Timor-Leste': 'Oceania',
    'Saint Kitts & Nevis': 'North America',
    'St. Vincent & Grenadines': 'North America',
    'Sao Tome & Principe': 'Africa',
    'Micronesia': 'Oceania'
}

# Map countries to continents
def get_continent(country_name):
    # Check in manual mapping first
    if country_name in manual_continent_mapping:
        return manual_continent_mapping[country_name]
    try:
        # Attempt to get the country object
        country = pycountry.countries.lookup(country_name)
        # Convert country alpha_2 to continent code
        continent_code = pc.country_alpha2_to_continent_code(country.alpha_2)
        # Convert continent code to continent name
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        return continent_name
    except (LookupError, KeyError):
        # Return None if the country is not found or any error occurs
        return None

# Apply function to the Country column
gdp_table['Continent'] = gdp_table['Country'].apply(get_continent)

# Identify unmapped countries after the automated mapping
unmapped_countries = gdp_table[gdp_table['Continent'].isnull()]['Country'].unique()

# Print unmapped countries (if any)
print("Unmapped Countries:", unmapped_countries)

# Update unmapped countries using manual mapping explicitly
for country in unmapped_countries:
    if country in manual_continent_mapping:
        gdp_table.loc[gdp_table['Country'] == country, 'Continent'] = manual_continent_mapping[country]

# Verify the updated DataFrame and check for any remaining unmapped rows
final_unmapped_countries = gdp_table[gdp_table['Continent'].isnull()]['Country'].unique()
print("Remaining Unmapped Countries:", final_unmapped_countries)

# Add a new column for the share of total population, and format as % with 2 decimal places
total_population_share = gdp_table['Population  (2022)'].sum()
gdp_table['Share of Total Population'] = (gdp_table['Population  (2022)'] / total_population_share).apply(lambda x: f"{x:.2%}")

# Save the updated DataFrame to a new CSV file
gdp_table.to_csv('gdp_by_country_with_continents.csv', index=False)
