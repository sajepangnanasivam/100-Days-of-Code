from Menu import *


# TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO: Currency conversion.
# TODO: Report() function for reporting remaining resources.
# TODO: function to check for enough resources. give appropriate message.
# TODO: IF there is enough resources for selected drink, prompt the user to insert coins.

def check_resources(drink):
    """
    Checks whether there is sufficient amount of resources.
    """
    enough_resources = True
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    chosen_drink = MENU[drink]

    if chosen_drink["ingredients"]["water"] > water:
        enough_resources = False
        print("Sorry, there is not enough Water..")
        return enough_resources
    elif chosen_drink["ingredients"]["coffee"] > coffee:
        enough_resources = False
        print("Sorry, there is not enough Coffee..")
        return enough_resources
    # TODO: Espresso does not contain Milk in the recipe. Need to adress the error handling.
    # elif chosen_drink["ingredients"]["milk"] > milk:
    #    enough_resources = False
    #    return "Sorry, there is not enough Milk."

    return enough_resources


def payment():
    """
    Function for making payment.
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
    current_drink_water = chosen_drink["ingredients"]["water"]
    #current_drink_milk = chosen_drink["ingredients"]["milk"]
    current_drink_coffee = chosen_drink["ingredients"]["coffee"]

    # Machine Resources
    machine_water = resources["water"]
    #machine_milk = resources["milk"]
    machine_coffee = resources["coffee"]

    # Subtracting the machine resources and updating dictionary.
    machine_water -= current_drink_water
    machine_coffee -= current_drink_coffee
    #machine_milk -= current_drink_milk
    print(f"\nRemaining water: {machine_water}\nRemaining coffee: {machine_coffee}")


# Program execution
continue_coffee_machine = True
while continue_coffee_machine:
    drink = input("What would you like? (espresso/latte/cappuccino):\t").lower()
    enough_resources = check_resources(drink)
    # if there is not enough resources, stop the program. Continue else.
    if not enough_resources:
        continue_coffee_machine = False
    else:
        customer_pay = payment()
        enough_money = check_payment(drink, customer_pay)
        if not enough_money:
            continue_coffee_machine = False
        else:
            make_coffee(drink)
