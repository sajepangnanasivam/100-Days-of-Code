#Write your code below this row 👇
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
# Thus, the first even number would be 2 and the last one is 100:

number = 0
for i in range(1, 101):
    if i % 2 == 0:
        number += i
print(number)

# Solution 2
number = 0
for i in range(2, 101, 2):
    number += i
print(number)