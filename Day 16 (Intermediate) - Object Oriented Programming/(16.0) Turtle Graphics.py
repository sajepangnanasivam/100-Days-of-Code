from turtle import Turtle, Screen, color
import random
# Timmy is an object, Turtle is a Class.
timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("red1")

timmy.speed(0)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)


for i in range(180):
    timmy.forward(300)
    timmy.right(624)
    timmy.forward(38)
    timmy.left(93)

    timmy.penup()
    timmy.setposition(0, 0)
    change_color()
    timmy.pendown()


my_screen = Screen()
my_screen.exitonclick()



