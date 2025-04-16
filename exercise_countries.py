countries = [
    {"name": "Japan", "population": 124_000_000},
    {"name": "Nepal", "population": 29_000_000},
    {"name": "India", "population": 1_438_000_000},
    {"name": "Sri Lanka", "population": 22_000_000},
    {"name": "France", "population": 68_000_000},
]
biggest_country = countries[0]
for index, country in enumerate(countries) :
    print(f"Index: {index}   - Name: {country["name"]} - Population: {country["population"]:,}")
    # Add a if to compare country with biggest_country
    # if true we store the country in biggest_country
    if country["population"] > biggest_country["population"]:
        biggest_country = country
    

# After the loop, we display the biggest country
print(f"The biggest country is {biggest_country["name"]} with a population of {biggest_country["population"]:,}")