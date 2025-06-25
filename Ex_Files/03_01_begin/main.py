import csv
from pprint import pprint

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

# Open the laureates.csv file for reading
with open("laureates.csv", "r") as f:
    # Create a DictReader to read the CSV file as dictionaries (each row becomes a dict)
    reader = csv.DictReader(f)
    # Convert the reader object to a list of dictionaries, one for each laureate
    laureates = list(reader)

for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        break
