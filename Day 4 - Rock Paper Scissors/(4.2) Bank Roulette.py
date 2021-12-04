import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
random_number = random.randint(0, len(names)-1)
random_person = names[random_number]

print(f"{random_person} is going to buy the meal today!")