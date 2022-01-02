from Menu import *


def check_resources(drink):
    """
    Checks whether there is sufficient amount of resources.
    """
    enough_resources = True
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    chosen_drink = MENU[drink]

    coffee_in_ingredients = "coffee" in MENU[drink]["ingredients"]
    milk_in_ingredients = "milk" in MENU[drink]["ingredients"]
    water_in_ingredients = "milk" in MENU[drink]["ingredients"]

    if water_in_ingredients and chosen_drink["ingredients"]["water"] > water:
        enough_resources = False
        print("Sorry, there is not enough Water..")
        return enough_resources
    if coffee_in_ingredients and (chosen_drink["ingredients"]["coffee"] > coffee):
        enough_resources = False
        print("Sorry, there is not enough Coffee..")
        return enough_resources
    if milk_in_ingredients and (chosen_drink["ingredients"]["milk"] > milk):
        print("Sorry, there is not enough Milk..")
        return enough_resources

    return enough_resources


def make_payment():
    """
    For making the payment.
    """
    print("💰 Please insert Coins: ")
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    quarters = float(input("💲 How many Quarters?:\t ")) * 0.25
    dimes = float(input("💲 How many dimes?:\t\t ")) * 0.10
    nickles = float(input("💲 How many nickles?:\t ")) * 0.05
    pennies = float(input("💲 How many pennies?:\t ")) * 0.01

    total_amount = quarters + dimes + nickles + pennies
    return total_amount


def check_payment(drink, customer_pay):
    """
    checks if the payment is suceeded.
    If the customer has paid more than the drink cost, calculate the differnece and refund money.
    """
    drink_cost = MENU[drink]["cost"]
    enough_money = True

    if drink_cost > customer_pay:
        print("Sorry, that's not enough money. Money Refunded.")
        enough_money = False
        return enough_money
    elif customer_pay > drink_cost:
        refund = round((customer_pay - drink_cost), 2)
        print(f"Thank you for your purchase, here is your refund of ${refund}")
    return enough_money


def make_coffee(drink):
    # Chosen Drink
    chosen_drink = MENU[drink]

    # Creating an instance of the machine resources.
    remaining_coffee = resources["coffee"]
    remaining_water = resources["water"]
    remaining_milk = resources["milk"]
    # Checking if the ingredients are in the drink's ingerdient list.
    if "milk" in MENU[drink]["ingredients"]:
        resources["milk"] -= chosen_drink["ingredients"]["milk"]
        remaining_milk = resources["milk"]
    if "coffee" in MENU[drink]["ingredients"]:
        resources["coffee"] -= chosen_drink["ingredients"]["coffee"]
        remaining_coffee = resources["coffee"]
    if "water" in MENU[drink]["ingredients"]:
        resources["water"] -= chosen_drink["ingredients"]["water"]
        remaining_water = resources["water"]

    return remaining_water, remaining_coffee, remaining_milk


def report(money_in_machine):
    """
    To print out a report when the customer types in "report".
    Shows remaining water, milk, coffee, and the total bill.
    """
    remaining_coffee = resources["coffee"]
    remaining_water = resources["water"]
    remaining_milk = resources["milk"]
    print(
        f"\n💧 Remaining water: \t{remaining_water}ml\n💧 Remaining milk: \t\t{remaining_milk}ml\n☕ Remaining coffee: \t{remaining_coffee}g\n💲 Money: {money_in_machine}")


def calculate_bill(drink, money_in_machine):
    money_in_machine += MENU[drink]["cost"]
    return money_in_machine


## --------------------------------- ##
## ------- Program execution ------- ##
## --------------------------------- ##
continue_coffee_machine = True
money_in_machine = 0
while continue_coffee_machine:
    drink = input("\nWhat would you like? (espresso/latte/cappuccino):\t").lower()
    if drink == "off":
        print("\n🛠 Machine turning off.. Ready for maintenance.")
        continue_coffee_machine = False
    elif drink == "report":
        report(money_in_machine)
    # if there is not enough resources, stop the program. Continue else.
    elif drink in ["espresso", "latte", "cappuccino"]:
        enough_resources = check_resources(drink)
        if not enough_resources:
            continue_coffee_machine = False
        else:
            # Everytime a user purchases a drink, the cost will be added to the bill.
            money_in_machine = calculate_bill(drink, money_in_machine)
            # Showing the customer what the cost for the drink is.
            cost = MENU[drink]["cost"]
            print(f"\nThe cost for {drink} is ${cost}")
            customer_pay = make_payment()
            enough_money = check_payment(drink, customer_pay)
            if not enough_money:
                continue_coffee_machine = False
            else:
                make_coffee(drink)
