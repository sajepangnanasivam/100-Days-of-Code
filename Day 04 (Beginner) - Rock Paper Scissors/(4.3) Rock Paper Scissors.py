rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_images = [rock, paper, scissors]

# For Users
choice_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


if choice_user >= 3 or choice_user < 0:
  print("Invalid number, try again.")
else:
  print(game_images[choice_user])

  # For PC
  choice_PC = random.randint(0, 2)
  print(f"Computer Chose:\n {game_images[choice_PC]}")

  if choice_user == 0 and choice_PC == 2:
    print("You Win!")
  elif choice_PC == 0 and choice_user == 2:
    print("You Lose")
  elif choice_PC > choice_user:
    print("You Lose!")
  elif choice_user > choice_PC:
    print("You Win!")
  elif choice_PC == choice_user:
    print("It's a Draw!")