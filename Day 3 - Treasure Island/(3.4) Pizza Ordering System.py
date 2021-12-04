# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

pizza_S = 15
pizza_M = 20
pizza_L = 25

pepperoni_S = 2
pepperoni_ML = 3
cheese = 1

# For Small Pizza
if size in ["S", "s"]:
    bill += pizza_S
    if add_pepperoni in ["y", "Y"]:
        bill += pepperoni_S
    if extra_cheese in ["y", "Y"]:
        bill += cheese
    print(f"Your final bill is: ${bill}.")

# For Medium Pizza
elif size in ["m", "M"]:
    bill += pizza_M
    if add_pepperoni in ["y", "Y"]:
        bill += pepperoni_ML
    if extra_cheese in ["y", "Y"]:
        bill += cheese
    print(f"Your final bill is: ${bill}.")

# For Large Pizza
elif size in ["l", "L"]:
    bill += pizza_L
    if add_pepperoni in ["y", "Y"]:
        bill += pepperoni_ML
    if extra_cheese in ["y", "Y"]:
        bill += cheese
    print(f"Your final bill is: ${bill}.")

else:
    print("Thank you for contacting us.")