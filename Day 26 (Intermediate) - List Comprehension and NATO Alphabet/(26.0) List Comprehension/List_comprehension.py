numbers = [1, 2, 3]
loop_list = []
for n in numbers:
    add_1 = n + 1
    loop_list.append(add_1)
print(loop_list)

# List comprehension
new_list = [n + 1 for n in numbers]
print(new_list)

# Example 2
name = "Sajepan"
letters_list = [letter for letter in name]
print(letters_list)

# Example 3
range_list = [num * 2 for num in range(1, 5)]
print(range_list)

# Example 4
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
upper_case = [name.upper() for name in names if len(name) > 5]

print(upper_case)
print(short_names)