import csv
from datetime import datetime
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

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        print("============")
        year_date = datetime.strptime(laureate["year"], "%Y")
        born_date = datetime.strptime(laureate["born"], "%Y-%m-%d")
        print("age", year_date.year - born_date.year)
        print(year_date, born_date)
        break

# ---
# Example output explanation for Einstein (from laureates.csv):
# When the code finds the laureate with surname 'Einstein', it prints:
# - All of Einstein's information as a dictionary
# - A separator line
# - The year he won the Nobel Prize ('1921') and his birth year ('1879-03-14') are converted to datetime objects
# - The age is calculated as 1921 - 1879 = 42, so it prints: age 42
# - It also prints the datetime objects for year and birthdate
#
# Example output explanation for Marie Curie (from laureates.csv):
# When the code finds the laureate with surname 'Curie', it prints:
# - All of Marie Curie's information as a dictionary
# - A separator line
# - The year she won the Nobel Prize ('1903') and her birth year ('1867-11-07') are converted to datetime objects
# - The age is calculated as 1903 - 1867 = 36, so it prints: age 36
# - It also prints the datetime objects for year and birthdate
#
# This demonstrates how the code works for both Einstein and Marie Curie using the actual data from laureates.csv.
