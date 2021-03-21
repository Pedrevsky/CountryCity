from revision import revise
import database
import printing_service


def immediately_add_country():
    add = "y"
    while add == "y":
        nation = input("Write a nation you want to add: ")
        capital = input(f"Write a capital of {nation}: ")
        database.add_country(nation, capital)
        add = input("Do you want to add another country? Type 'y' if yes: ").lower()


def immediately_remove_country():
    nation = input("Write a nation you want to delete: ")
    database.remove_country(nation)


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
    #database.create_countries_file()
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
        elif choice == "33":
            print(database.get_all_countries())
        else:
            print("Unknown choice, please try again")
        choice = input(USER_CHOICE).lower()


menu()
