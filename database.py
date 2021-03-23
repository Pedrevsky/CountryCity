import json


countries_file = "countries.json"


def create_countries_file():
    with open(countries_file, "w") as file:
        json.dump([], file)


def get_all_countries():
    with open(countries_file, "r") as file:
        return json.load(file)


def add_country(country, capital):
    countries = get_all_countries()
    countries.append({"country": country, "capital": capital})
    _save_all_countries(countries)


def _save_all_countries(countries):
    with open(countries_file, "w") as file:
        json.dump(countries, file)


def remove_country(country):
    countries = get_all_countries()
    countries = [_country for _country in countries if _country['country'] != country]
    _save_all_countries(countries)
