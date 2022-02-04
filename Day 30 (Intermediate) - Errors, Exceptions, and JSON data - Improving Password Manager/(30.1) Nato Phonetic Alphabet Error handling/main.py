import pandas as pd

NATO_alphabet_data = pd.read_csv("nato_phonetic_alphabet.csv")

NATO_dict = {row.letter: row.code for (index, row) in NATO_alphabet_data.iterrows()}
print(NATO_dict)


def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        output_list = [NATO_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


continue_typing = True
while continue_typing:
    user_input = input("\n❓ Do you want to type? Yes/No\t").lower()
    if user_input == "yes":
        generate_phonetic()
    else:
        continue_typing = False

# --- Second Method ---#
# continue_typing = True
# while continue_typing:
#     user_word = input("Enter a word: ").upper()
#     try:
#         output_list = [NATO_dict[letter] for letter in user_word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#     else:
#         print(output_list)
#         continue_typing = False
