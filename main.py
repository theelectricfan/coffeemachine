MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
profit = 0


def printReport():
    for item in resources:
        print(f"{item}: {resources[item]}")
    print(f"Money: ${profit}")


def resourceSufficient(drink):
    for item in resources:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry there is not enough {item}")
            return False

    return True


def insertCoins():
    quarterCount = int(input("Number of quarter inserted: "))
    dimeCount = int(input("Number of dime inserted: "))
    nickleCount = int(input("Number of nickle inserted: "))
    pennyCount = int(input("Number of penny inserted: "))
    return quarterCount * 0.25 + dimeCount * 0.10 + nickleCount * 0.05 + pennyCount * 0.01


def makeCoffee(drink):
    for item in resources:
        resources[item] -= MENU[drink]['ingredients'][item]
    print(f"Here is your {drink}. Enjoy!")


def choice():
    global profit
    while True:
        choiceInput = input("What would you like? (espresso/latte/cappuccino):").lower()
        if choiceInput == 'espresso' or choiceInput == 'latte' or choiceInput == 'cappuccino':
            if resourceSufficient(choiceInput):
                money = insertCoins()
                if money < MENU[choiceInput]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    if money > MENU[choiceInput]["cost"]:
                        print(f"Here is ${money - MENU[choiceInput]['cost']} in change.")
                    profit += MENU[choiceInput]["cost"]
                    makeCoffee(choiceInput)
        elif choiceInput == 'off':
            return
        elif choiceInput == 'report':
            printReport()
        else:
            print("Invalid input! Please try again.")


choice()
