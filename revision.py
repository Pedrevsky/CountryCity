import random
import database

countries = database.get_all_countries()


def if_empty(countries):
    if len(countries) == 0:
        print("List is empty")
    else:
        nation_or_capital()


def nation_or_capital():
    decision = input("What would you like to revise? For capitals press 1, for nations press 2: ")
    new_countries = database.get_all_countries()
    random_country = random.choice(new_countries)
    if decision == "1":
        value = 'capital'
        key = 'nation'
    elif decision == "2":
        value = 'nation'
        key = 'capital'
    else:
        print("Unknown choice")
        value = 'capital'
        key = 'nation'
    while decision == "1" or decision == "2":
        guess = input(f"{random_country[key]} - ")
        while guess != "EXIT":
            if guess == random_country[value]:
                print("You are right!")
                random_country = random.choice(new_countries)
                guess = input(f"{random_country[key]} - ")
            else:
                print("You are wrong")
                if decision == "1":
                    print(f"Capital of {random_country['nation']} is {random_country['capital']}")
                    random_country = random.choice(new_countries)
                    guess = input(f"{random_country[key]} - ")
                elif decision == "2":
                    print(f"{random_country['capital']} is capital of {random_country['nation']}")
                    random_country = random.choice(new_countries)
                    guess = input(f"{random_country[key]} - ")


def revise():
    if_empty(countries)
