#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")

amount = input("What was the total bill?")
tip = input("How much tip would you like to give?")
people = input("How many people to split the bill?")

calculation = (float(amount) / float(people)) * ((float(tip) / 100) + 1)
# including only two decimal points. Can be also done with round(calculation, 2).
final_amount = "{:.2f}".format(calculation)
print(f"Each person should pay ${final_amount}")