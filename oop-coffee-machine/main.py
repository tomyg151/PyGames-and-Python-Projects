from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

# Build all the objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


def coffee_machine():
    print(logo)

    # print users choices
    options = menu.get_items()
    user_choice = input(f"What would you like? {options}: ").lower()

    while user_choice != "off":

        # input user choice (check if user_choice is report or a coffee)
        if user_choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif menu.find_drink(user_choice) is not None:
            # drink = Coffee_objects  --> user_choice already checked if it is a coffee or not!!!
            drink = menu.find_drink(user_choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        user_choice = input(f"What would you like? {options}: ").lower()
    print("Thank you and goodbye 😃")


coffee_machine()
