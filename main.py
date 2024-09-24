#NOT GOOD. LOOKS LIKE A 5 YEARS OLD'S CODE. NEED TO MODIFY.
#NOT GOOD. LOOKS LIKE A 5 YEARS OLD'S CODE. NEED TO MODIFY.
#NOT GOOD. LOOKS LIKE A 5 YEARS OLD'S CODE. NEED TO MODIFY.
#NOT GOOD. LOOKS LIKE A 5 YEARS OLD'S CODE. NEED TO MODIFY.
#NOT GOOD. LOOKS LIKE A 5 YEARS OLD'S CODE. NEED TO MODIFY.
#NOT GOOD. LOOKS LIKE A 5 YEARS OLD'S CODE. NEED TO MODIFY.
#NOT GOOD. LOOKS LIKE A 5 YEARS OLD'S CODE. NEED TO MODIFY.
#NOT GOOD. LOOKS LIKE A 5 YEARS OLD'S CODE. NEED TO MODIFY.
#NOT GOOD. LOOKS LIKE A 5 YEARS OLD'S CODE. NEED TO MODIFY.
#NOT GOOD. LOOKS LIKE A 5 YEARS OLD'S CODE. NEED TO MODIFY.

MENU = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino":{
        "ingredients":{
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
    "money": 0
}


while True:
    #TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    #TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
    if prompt == "off":
        exit()

    #TODO 3: Print report
    if prompt == "report":
        for item in resources:
           print(f"{item}: {resources[item]}")
        exit()

    #TODO 4: Check resources sufficient?
    for item in MENU:
        if MENU[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")

    #TODO 5: Process coins.
    print("Please insert coins.")
    penny = int(input("How many pennies?: "))
    nickel = int(input("How many nickels?: "))
    dime = int(input("How many dimes?: "))
    quarter = int(input("How many quarters?: "))

    totalMoney = (penny * 0.01) + (nickel * 0.05) + (dime * 0.10) + (quarter * 0.25)

    #TODO 6: Check transaction successful?
    if MENU[prompt]["cost"] > totalMoney:
        print(f"Sorry, that's not enough money. Money refunded.")
        exit()

    elif MENU[prompt]["cost"] == totalMoney:
        resources["money"] += MENU[prompt]["cost"]

    elif MENU[prompt]["cost"] < totalMoney:
        resources["money"] += MENU[prompt]["cost"]
        change = totalMoney - MENU[prompt]["cost"]
        print(f"Here is {change:.2f} in change.")

    #TODO 7: Make Coffee.
    if prompt == ("espresso" or "latte" or "cappuccino"):
        resources["water"] -= MENU[prompt]["ingredients"]["water"]
        resources["coffee"] -= MENU[prompt]["ingredients"]["coffee"]

    if prompt == ("latte" or "cappuccino"):
        resources["milk"] -= MENU[prompt]["ingredients"]["milk"]

    print(f"Here is your {prompt}. Enjoy!")