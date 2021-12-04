print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0
if height > 120:
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print(f"\nYou are under 12, ticket price is ${bill}\n")
  
  elif age <= 18:
    bill = 7
    print(f"\nYour age is between 12 and 18, ticket price is ${bill}\n")

  else:
    bill = 12
    print(f"\nYour age is {age}, ticket price is $12\n")

  photo = input("Do you want photo for $3?, 'Y' or 'N': ")

  if photo in ["y", "Y", "yes", "Yes", "YES"]:
    bill += 3
    print(f"Your total bill comes at ${bill}. Please collect your photo at the reception!")
    
  elif photo in ["n", "N", "no", "No", "N"]:
    print(f"Thank you for riding with us, your total bill is ${bill}")
else:
  print("You can't ride")