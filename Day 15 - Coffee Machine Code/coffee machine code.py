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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

amount = 0

def report():
    print(f"Water {resources['water']}ml")
    print(f"Milk {resources['milk']}ml")
    print(f"Coffee {resources['coffee']}g")
    print(f"Money: ${profit}")


def resources_checker():
    if resources["water"] >= MENU[user_ans]["ingredients"]["water"]:
        resources["water"] -= MENU[user_ans]["ingredients"]["water"]
        resources["coffee"] -= MENU[user_ans]["ingredients"]["coffee"]
        try:
            resources["milk"] -= MENU[user_ans]["ingredients"]["milk"]
        except KeyError:
            return None
    else:
        return "deactivate"

def currency():
    global profit
    global total
    global change

    print("Please insert coins")
    quarters =float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    total= quarters + nickles + dimes + pennies
    change = round(total - MENU[user_ans]["cost"]-0.50, 2)
    profit += change + 0.50

def sufficent_balance():
    if (MENU[user_ans]["cost"]+1) <= total:
        print(f"Here is ${change} in change.")
        print(f"Here is you {user_ans} ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


running = True
while running:
    user_ans = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()
    if user_ans in ("espresso", "latte", "cappuccino"):
        if resources_checker() != "deactivate":
            currency()
            sufficent_balance()
        else:
            print("Sorry there's not enough water.")
        # deduct()
    elif user_ans == 'report':
        report()
    elif user_ans == "off":
        running = False
