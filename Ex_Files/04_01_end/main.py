import requests
from pprint import pprint

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

data = response.json()[1][:50]  # Get last 50 years

def safe_value(val):
    return val if val is not None else 0

# Calculate 5-year averages
for i in range(0, 50, 5):
    group = data[i:i+5]
    values = [year["value"] for year in group if year["value"] is not None]
    if values:
        avg = sum(values) // len(values)
        years = f'{group[-1]["date"]}-{group[0]["date"]}'
        print(f"{years}: 5-year average population: {avg}","Years with values",len(values))
    else:
        years = f'{group[-1]["date"]}-{group[0]["date"]}'
        print(f"{years}: No data for 5-year average")
