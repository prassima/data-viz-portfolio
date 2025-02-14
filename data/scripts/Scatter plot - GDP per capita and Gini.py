import pandas as pd

# URL of the webpage containing the table
gdp_url = 'https://www.worldometers.info/gdp/gdp-by-country/'
gdp = pd.read_html(gdp_url)

# The first/only table is the one we want
gdp_table = gdp[0]
gdp_table.drop(columns=['GDP  (abbrev.)','#'], axis=1, inplace=True)

## Get Gini Coefficient data
gini_url = 'https://worldpopulationreview.com/country-rankings/gini-coefficient-by-country'
gini = pd.read_html(gini_url)

# The 3rd table is the one we want
gini_table = gini[2]

# Get countries benefiting from racist world
race_url = 'https://worldpopulationreview.com/country-rankings/caucasian-countries'
race = pd.read_html(race_url)
# We want 2nd table
race_table = race[1]
# Add column to identify majority white countries, and drop continent
race_table["Majority 'white' country"]=True
race_table.drop(columns=['Continent', 'Caucasian'], axis=1, inplace=True)

# Merge the various DataFrames on the 'Country' column
merged_table = gdp_table.merge(gini_table, left_on='Country', right_on='Country', how='left')
merged_table['Gini coefficient']=merged_table['Gini Coefficient - World Bank'].fillna(merged_table['Gini Coefficient - CIA World Factbook'])
merged_table = merged_table.merge(race_table, left_on='Country', right_on='Country', how='left')
merged_table.drop(columns=['Gini Coefficient - World Bank','Gini Coefficient - CIA World Factbook','Data Year (World Bank)','Data Year (CIA)'], axis=1, inplace=True)
merged_table["Majority 'white' country"]=merged_table["Majority 'white' country"].fillna(False)

# Save the updated DataFrame to a new CSV file
merged_table.to_csv('./data/output/Scatter plot - GDP per capita and Gini.csv', index=False)