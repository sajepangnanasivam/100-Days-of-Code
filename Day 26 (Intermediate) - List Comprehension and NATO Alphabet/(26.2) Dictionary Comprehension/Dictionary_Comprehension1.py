import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# Exercise 1
# student_scores = {new_key:new_value for item in list}
student_scores = {student: random.randint(1, 100) for student in names}

print(f"Student Scores:\t\t {student_scores}")

# Exercise 2
# passed_students = {new_key:new_value for (key, value) in dict.items() if}
passed_students = {student: score for (student, score) in student_scores.items() if score > 60}

print(f"Passed students:\t {passed_students}")

# Exercise 3
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
words = sentence.split()
result = {word: len(word) for word in words}
print(result)

# Exercise 4
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


# 🚨 Don't change code above 👆
def celsius_to_fahrenheit(temp_c):
    return (temp_c * 9 / 5) + 32

weather_f = {day: celsius_to_fahrenheit(temp_c) for (day, temp_c) in weather_c.items()}
print(weather_f)
