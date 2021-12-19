from replit import clear
from art import logo

# Printing logo
print(logo)

# Initiation of an empty dictionary
bids = {}
continue_bid = True

def find_highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    # Gets the value from each key
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner}, with a bid of ${highest_bid}")

while continue_bid:
  # Asking for user input
  name = input("Enter your name: ").lower()
  bid = int(input("Enter your bid price: $"))

  # Creating an empty dictionary then adding name(key) and the bid(value)
  bids[name] = bid
  
  # Asking the user if they want to place an another bid.
  new_bid = input("Enter 'Yes' to place more bids. Otherwise type 'No'").lower()
  if new_bid == "yes":
    clear()
  elif new_bid == "no":
    continue_bid = False
    find_highest_bidder(bids)
    
  
  
  