# Menu Items

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    'Money': 0
}

DRINK_MADE = False
MACHINE_ON = True
HAVE_ORDER = False

while MACHINE_ON:
    # TODO 0. Prompt user for order
    print("What would you like? (espresso/latte/cappuccino):")
    order = input()

    # TODO 1. Print a report of all coffee recourses
    if order == 'espresso' or order == 'latte' or order == 'cappuccino':
        HAVE_ORDER = True
    if order == 'report':
        for k, v in resources.items():
            print(k, ':', v)
    if order == 'off':
        print("Bye!")
        MACHINE_ON = False
        break

    # TODO 2. Check resources sufficient in the machine

    while HAVE_ORDER:
        Enough_Resources = True
        # Check what order was chosen
        if order == 'espresso':
            if resources['water'] <= MENU['espresso']['ingredients']['water']:
                Enough_Resources = False
            elif resources['coffee'] <= MENU['espresso']['ingredients']['coffee']:
                Enough_Resources = False
        if order == 'latte':
            if resources['water'] <= MENU['latte']['ingredients']['water']:
                Enough_Resources = False
            elif resources['milk'] <= MENU['latte']['ingredients']['milk']:
                Enough_Resources = False
            elif resources['coffee'] <= MENU['latte']['ingredients']['coffee']:
                Enough_Resources = False
        if order == 'cappuccino':
            if resources['water'] <= MENU['cappuccino']['ingredients']['water']:
                Enough_Resources = False
            elif resources['milk'] <= MENU['cappuccino']['ingredients']['milk']:
                Enough_Resources = False
            elif resources['coffee'] <= MENU['cappuccino']['ingredients']['coffee']:
                Enough_Resources = False
        if Enough_Resources == False:
            print('There are not enough condiments in the machine. Please refill and try again.')
            break
        # TODO 3. Process Coins.
        print(
            f"There are sufficient resources to make the drink. Please enter your funds of ${MENU[order]['cost']} for a {order}.")
        print('Please insert coins.')
        print('How many quarters?: ')
        quarters = int(input()) * 0.25
        print('How many dimes?: ')
        dimes = int(input()) * 0.1
        print('How many nickles?: ')
        nickles = int(input()) * 0.05
        print('How many pennies?: ')
        pennies = int(input())
        total = quarters + dimes + nickles + pennies

        # TODO 4. Check transaction successful
        if total >= MENU[order]['cost']:
            DRINK_MADE = True
            print(f'Here is your {order}, Enjoy!')
            print(f'Here is ${total - MENU[order]["cost"]} in change.')
        else:
            print("Sorry that's not enough money. Money refunded")
            HAVE_ORDER = False

        # TODO 5. Make Coffee and output message to user. Deduct ingredients

        if DRINK_MADE:
            # Deduct ingredients and add to money
            for k_machine, v_machine in resources.items():
                if (k_machine == 'water'):
                    resources['water'] -= MENU[order]['ingredients']['water']
                elif k_machine == 'milk' and order != 'espresso':
                    resources['milk'] -= MENU[order]['ingredients']['milk']
                elif k_machine == 'coffee':
                    resources['coffee'] -= MENU[order]['ingredients']['coffee']
                elif k_machine == 'Money':
                    resources['Money'] += MENU[order]['cost']

            for k, v in resources.items():
                print(k, ':', v)

            DRINK_MADE = False
            HAVE_ORDER = False
