import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL of the webpage containing the GDP table
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

# Get table classifying various 'Western' countries
western_url = "https://worldpopulationreview.com/country-rankings/western-countries"
western_response = requests.get(western_url)
western_html_content = western_response.content
soup = BeautifulSoup(western_html_content, "html.parser")

# Locate the table
western_table = soup.find("table")  # Adjust if there multiple tables arise

# Extract rows
rows = []
for row in western_table.find_all("tr")[1:]:  # Skip the header row
    cells = row.find_all(["th", "td"])
    row_data = []
    for cell in cells:
        # Check for SVG icons
        svg = cell.find("svg")
        if svg:
            if "tabler-icon-x" in svg.get("class", []):
                row_data.append(False)
            elif "tabler-icon-check" in svg.get("class", []):
                row_data.append(True)
            else:
                row_data.append(None)  # Handle unexpected cases
        else:
            row_data.append(cell.text.strip())
    rows.append(row_data)

# Create a DataFrame
western = pd.DataFrame(rows)
western.rename(columns=
          {0: 'Country', 
           1: 'Latin West', 
           2: 'Cold War West', 
           3: 'Rich West', 
           4: 'Western Europe', 
           5: 'Western Hemisphere'},
          inplace=True)


# Merge the various DataFrames on the 'Country' column
merged_table = gdp_table.merge(gini_table, left_on='Country', right_on='Country', how='left')
merged_table['Gini coefficient']=merged_table['Gini Coefficient - World Bank'].fillna(merged_table['Gini Coefficient - CIA World Factbook'])
merged_table = merged_table.merge(race_table, left_on='Country', right_on='Country', how='left')
merged_table = merged_table.merge(western, left_on='Country', right_on='Country', how='left')
merged_table.fillna(False, inplace=True)
merged_table.drop(columns=['Gini Coefficient - World Bank','Gini Coefficient - CIA World Factbook','Data Year (World Bank)','Data Year (CIA)'], axis=1, inplace=True)
merged_table["Majority 'white' country"]=merged_table["Majority 'white' country"].fillna(False)

# Save the updated DataFrame to a new CSV file
merged_table.to_csv('./data/output/Scatter plot - GDP per capita and Gini.csv', index=False)