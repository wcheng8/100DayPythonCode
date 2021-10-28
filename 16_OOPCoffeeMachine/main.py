from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Instantiate objects
menu = Menu()
coffee_bank = MoneyMachine()
coffee_machine = CoffeeMaker()
enough_resource = True

while enough_resource:
    # TODO 1: Print report
    order = input(f"What would you like? ({menu.get_items()}): ")

    # Check if the drink is in the menu
    drink = menu.find_drink(order)

    # Rename constants
    if drink:
        water = drink.ingredients['water']
        milk = drink.ingredients['water']
        coffee = drink.ingredients['water']
        cost = drink.cost

    if order == 'report':
        coffee_machine.report()

    if order == 'off':
        break

    # TODO 2: Check resources sufficient?

    if not coffee_machine.is_resource_sufficient(drink):
        break

    # TODO 3: Process Coins
    # TODO 4: Check transaction successful?

    if coffee_bank.make_payment(cost):

    # TODO 5: Make Coffee.
        coffee_machine.make_coffee(drink)
        coffee_machine.report()