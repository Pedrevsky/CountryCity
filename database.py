import json


countries_file = "countries.json"


# def create_countries_file():
#     with open(countries_file, "w") as file:
#         json.dump([], file)


def get_all_countries():
    with open(countries_file, "r") as file:
        return json.load(file)


def add_country(nation, capital):
    countries = get_all_countries()
    countries.append({"nation": nation, "capital": capital})
    _save_all_countries(countries)


def _save_all_countries(countries):
    with open(countries_file, "w") as file:
        json.dump(countries, file)


def remove_country(nation):
    countries = get_all_countries()
    countries = [country for country in countries if country['nation'] != nation]
    _save_all_countries(countries)
