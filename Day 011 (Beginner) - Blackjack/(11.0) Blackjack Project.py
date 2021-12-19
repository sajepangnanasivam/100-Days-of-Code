###############################################################
################### Blackjack Project #########################
###############################################################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###############################################################
import random
from art import logo
from replit import clear


# Available card deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# Defining some of the game rules
ace11 = cards[0]
ace1 = 1

def deal_card():
  """ Returns a random card from the deck """

  random_card = random.choice(cards)
  return random_card

# check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 
# 0 will represent a blackjack in our game.
def calculate_score(cards):
  """ Take a list of cards and return the score calculated from the cards."""
  # check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
  score = sum(cards)
  if score == 21 and len(cards) == 2:
    return 0
  if ace11 in cards and score > 21:
    cards.remove(ace11)
    cards.append(ace1)
  return score

def compare(user_score, computer_score):
  """ Compares the user and computer scores and returns a winner. """
  if user_score == computer_score:
    return "🔘 It's a Draw!\n"
  elif computer_score == 0:
    return "❌ You lose, opponent has Blackjack.\n"
  elif user_score == 0:
    return "✅ You win with a Blackjack!\n"
  elif user_score > 21:
    return "❌ You lose, you went over.\n"
  elif computer_score > 21:
    return "✅ You win, opponent went over!\n"
  elif user_score > computer_score:
    return "✅ You win!\n"
  else:
    return "❌ You lose..\n"

def play_blackjack():
  """ Play the game """
  print(logo)
  # Initiating empty lists as a starting point
  user_cards = []
  computer_cards = []

  # Dealing 2 cards each for the players.
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  is_game_over = False
  while not is_game_over:
    # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # Just printing to check the values
    print(f"User cards:\t\t {user_cards} - score: {user_score}")
    print(f" Computer's First card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  # Once the user is done, it's time to let the computer play. 
  # The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"\n\tYou final hand: {user_cards}\t Final Score: {user_score}")
  print(f"\tComputer's final hand: {computer_cards}\t Final Score: {computer_score}\n")
  print(compare(user_score, computer_score))

# Giving the user the ability to play the game over and over again.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  clear()
  play_blackjack()
  
  