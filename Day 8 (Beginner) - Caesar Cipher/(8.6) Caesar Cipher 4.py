alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char

  print(f"Here's the {cipher_direction}d result: {end_text}\n")
  
#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again.
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #program continues to work even if the user enters a shift number greater than 26. 
  shift = shift % len(alphabet)
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  rerun = input("Type 'Yes' if you want to encode/decode. Otherwise type 'No': ")
  
  if rerun == "no":
    should_continue = False
    print("Goodbye")