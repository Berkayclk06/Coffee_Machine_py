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
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}


def make_coffee(coffee: str):
    for ing in resources:
        if user_choice == "espresso" and ing == "milk":
            pass
        else:
            resources[ing] = resources[ing] - MENU[coffee]["ingredients"][ing]
    print(f"Here is your {coffee}. Enjoy!")


def resource_sufficient(wat: int, mil: int, cof: int):
    if resources["water"] < wat:
        print(f"Sorry not enough water")
        return "0"

    elif resources["coffee"] < cof:
        print(f"Sorry not enough coffee")
        return "0"

    elif resources["milk"] < mil:
        print(f"Sorry not enough milk")
        return "0"
    else:
        return "1"


start = True
money = 0
resource_money = 0
# TODO 1. Prompt user by asking "What would you like? (Espresso/latte/capuccino):"
while start:
    user_choice = input("What would you like? (Espresso/latte/cappuccino): ").lower()

    if user_choice != "espresso" and user_choice != "latte" and user_choice != "cappuccino" and user_choice != "report"\
            and user_choice != "off":
        print("You have entered a wrong input. Please try again.")
        continue

    # TODO 2. Turn off the Coffee Machine by entering "off" to the prompt.
    if user_choice == "off":
        start = False

    # TODO 3. Print report.
    if user_choice == "report":
        for item in resources:
            if item == "coffee":
                print(f"{item.capitalize()}: {resources[item]}g")
            else:
                print(f"{item.capitalize()}: {resources[item]}ml")
        print(f"Money: ${resource_money}")
        continue

    # TODO 4. Check resources sufficient?
    if user_choice != "report" and user_choice != "off":
        if "milk" in MENU[user_choice]["ingredients"]:
            suf = resource_sufficient(MENU[user_choice]["ingredients"]["water"], MENU[user_choice]["ingredients"]["milk"],
                                      MENU[user_choice]["ingredients"]["coffee"])
        else:
            suf = resource_sufficient(MENU[user_choice]["ingredients"]["water"], resources["milk"],
                                      MENU[user_choice]["ingredients"]["coffee"])
        if suf == "0":
            continue
        elif suf == "1":
            print(f"Please insert coins.\nYour choice: {user_choice.capitalize()}\nTotal Balance: ${MENU[user_choice]['cost']}")
    # TODO 5. Process coins.
    for items in coins:
        inserted = int(input(f"How many {items}?: "))
        money += coins[items] * inserted

    # TODO 6. Check transaction successful?
    if money < MENU[user_choice]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        money = 0
        continue

    elif money > MENU[user_choice]['cost']:
        resource_money += MENU[user_choice]['cost']
        change = (money - MENU[user_choice]['cost'])
        print(f"Here is ${round(change, 2)} in change.")
        money = 0
    else:
        resource_money += money
        money = 0

    # TODO 7. Make Coffee

    make_coffee(user_choice)
