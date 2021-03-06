import random
from replit import clear
from art import logo
print(logo)

print("Welcome to the number guessing game!")
print("🤔 \tI'm thinking of a number between 1 and 100.")

def guess_the_number(easy_or_hard):
  """The game start"""
  # Or random_number = randint(1, 100)
  random_number = random.choice(range(1, 101))
  #print(random_number)
  continue_game = True
  attempts = easy_or_hard

  while continue_game:
    if attempts == 0:
      continue_game = False
      print(f"\n❌ You lost, The number is {random_number}\n")
      return
    
    print(f"You have {attempts} attempts.")
    guess = int(input("Make a guess: "))

    if guess > random_number:
      attempts -= 1
      print("\n⬆️ \tToo High.")
    elif guess < random_number:
      attempts -= 1
      print("\n⬇️ \tToo low.")
    else:
      continue_game = False
      print(f"\n✅ Correct! The number is {random_number}\n")
      

def initiate_game_with_difficulty():
  """To choose difficulty for the game, and start game by calling main game function"""
  difficulty = input("❓ \tChoose a difficulty. Type 'Easy' or 'Hard': ").lower()
  easy, hard = 10, 5
  if difficulty == "easy":
    print("\n👶 \tEasy Difficulty \t👶")
    guess_the_number(easy)
  else:
    print("\n⚔️ \tHard Difficulty\t ⚔️")
    guess_the_number(hard)

while input("❓ \tDo you want to play? Type 'y' or 'n': ").lower() == "y":
  clear()
  initiate_game_with_difficulty()