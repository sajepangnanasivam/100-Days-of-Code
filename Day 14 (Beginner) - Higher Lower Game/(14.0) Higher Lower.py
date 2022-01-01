from game_data import data
import random
from art import logo, vs
#from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(choice, follower_countA, follower_countB):
  """Checks followers against user's choice 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if follower_countA > follower_countB:
    return choice == "a"
  else:
    return choice == "b"


def game():
  print(logo)
  score = 0
  continue_game = True
  account_a = get_random_account()
  account_b = get_random_account()

  while continue_game:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      continue_game = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()

