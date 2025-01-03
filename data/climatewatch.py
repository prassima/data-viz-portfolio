##make sure you have all required packages in your current python environment. Run this in terminal: pip install -r requirements.txt
import pandas as pd
import requests

# Define the API endpoint
url = 'https://www.climatewatchdata.org/api/v1/data/historical_emissions'

# Set up the query parameters
params = {
    'start_year': 1990,
    'end_year': 2020,
    # Add other parameters as needed
}

# Make the GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Process the data as needed
    print(data)
else:
    print(f'Error: {response.status_code}')

records = data.get('data', [])  # Safely extract the list of dictionaries

df = pd.DataFrame(records)