#ensure all libraries are installed: in terminal (mac) or command line (win), run the following `pip install -r requirements.txt`
#for this script, the libraries are: pandas pycountry pycountry-convert
import pandas as pd
import pycountry
import pycountry_convert as pc

# URL of the webpage containing the table
gdp_url = 'https://www.worldometers.info/gdp/gdp-by-country/'
gdp = pd.read_html(gdp_url)

# The first/only table is the one we want
gdp_table = gdp[0]

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

# Function to map countries to continents
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

# Apply the function to the 'Country' column
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
gdp_table.drop(columns=['GDP  (abbrev.)','#'], axis=1, inplace=True)

## Get Gini Coefficient data
gini_url = 'https://worldpopulationreview.com/country-rankings/gini-coefficient-by-country'
gini = pd.read_html(gini_url)

# The 3rd table is the one we want
gini_table = gini[2]

# Get racist countries
race_url = 'https://worldpopulationreview.com/country-rankings/caucasian-countries'
race = pd.read_html(race_url)
# We want 2nd table
race_table = race[1]
# Add column to identify racist countries, and drop continent
race_table['Caucasian']=True
race_table.drop(columns=['Continent'], axis=1, inplace=True)

# Merge the various DataFrames on the 'Country' column
merged_table = gdp_table.merge(gini_table, left_on='Country', right_on='Country', how='left')
merged_table['Gini coefficient']=merged_table['Gini Coefficient - World Bank'].fillna(merged_table['Gini Coefficient - CIA World Factbook'])
merged_table = merged_table.merge(race_table, left_on='Country', right_on='Country', how='left')
merged_table.drop(columns=['Gini Coefficient - World Bank','Gini Coefficient - CIA World Factbook','Data Year (World Bank)','Data Year (CIA)'], axis=1, inplace=True)

# Save the updated DataFrame to a new CSV file
merged_table.to_csv('data/gdp_gini_race.csv', index=False)
