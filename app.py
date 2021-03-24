from revision import revise
import database
import printing_service


def immediately_add_country():
    add = "y"
    while add == "y":
        country = input("Write a country you want to add: ")
        capital = input(f"Write a capital of {country}: ")
        database.add_country(country, capital)
        add = input("Do you want to add another country? Type 'y' if yes, type anything else if no: ").lower()


def immediately_remove_country():
    country = input("Write a country you want to delete: ")
    database.remove_country(country)


USER_CHOICE = """
Welcome to app for revising countries and their capitals!
There are options:

-p) to see information about project
-i) to view instructions
-r) to start revising 
-a) to add a country
-d) to delete a country
-q) to quit

Your choice: """


def menu():
    #database.create_countries_file()       #This is used if there is no file: countries.json
    choice = input(USER_CHOICE).lower()
    while choice != "q":
        if choice == "p":
            printing_service.view_information()
        elif choice == "i":
            printing_service.view_instructions()
        elif choice == "r":
            revise()
        elif choice == "a":
            immediately_add_country()
        elif choice == "d":
            immediately_remove_country()
        elif choice == "3333": #This undercover option to check all countries we have saved
            print(database.get_all_countries())
        else:
            print("Unknown choice, please try again")
        choice = input(USER_CHOICE).lower()


menu()
