import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# TODO 1. Create a dictionary in this format:
NATO_alphabet_data = pd.read_csv("nato_phonetic_alphabet.csv")
# {new_key:new_value for (index, row) in df.iterrows()}
NATO_dict = {row.letter: row.code for (index, row) in NATO_alphabet_data.iterrows()}
print(NATO_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()
output_list = [NATO_dict[letter] for letter in user_word]

print(output_list)
