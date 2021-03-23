import random
import database

countries = database.get_all_countries()


def if_empty(countries):
    if len(countries) == 0:
        print("List is empty")
    else:
        country_or_capital()


def country_or_capital():

    decision = input("What would you like to revise? For capitals press 1, for countries press 2: ")
    while decision == "1" or decision == "2":

        new_countries = database.get_all_countries()
        random_country = random.choice(new_countries)
        if decision == "1":
            value, key = 'capital', 'country'
        elif decision == "2":
            value, key = 'country', 'capital'
        else:
            break
        guess = input(f"{random_country[key]} - ")
        if guess == "EXIT":
            break
        while decision == "1" or decision == "2" :
            if guess == "EXIT":
                break
            elif guess == random_country[value]:
                print("You are right!")
                random_country = random.choice(new_countries)
                guess = input(f"{random_country[key]} - ")
            else:
                print("You are wrong")
                if decision == "1":
                    print(f"Capital of {random_country['country']} is {random_country['capital']}")
                    random_country = random.choice(new_countries)
                    guess = input(f"{random_country[key]} - ")
                elif decision == "2":
                    print(f"{random_country['capital']} is capital of {random_country['country']}")
                    random_country = random.choice(new_countries)
                    guess = input(f"{random_country[key]} - ")
    else:
        print("Unknown choice")


def revise():
    if_empty(countries)
