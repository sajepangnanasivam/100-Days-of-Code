# --- Example 1 --- #
# FileNotFound and keyerror
try:
    file = open("a_file.txt")
    a_dict = {"Key": "This is the key value"}
    print(a_dict["Key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that i made up")
    file.close()
    print("File was closed..")

# --- Example 2 --- #
height = float(input("Height:\t"))
weight = int(input("weight:\t "))

if height > 3:
    raise ValueError(f"Inputted height is {height} meters, it should not be over 3 meters")

bmi = weight / (height ** 2)
print(bmi)

# --- Example 3 --- #
fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)

# --- Example 4 --- #
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)
