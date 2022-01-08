import random
import turtle as t
from turtle import Screen
from random import choice, randint

tim = t.Turtle()
tim.color("black")
tim.pensize(1.5)
tim.speed(0)

# Changing the shape to Doge
t.register_shape("doge(45x45).gif")
tim.shape("doge(45x45).gif")
tim.shapesize(1)

colors = ["indian red", "navajo white", "olive drab", "yellow green",
          "cadet blue", "dodger blue", "cornflower blue", "medium orchid",
          "DarkOrchid", "wheat", "SlateGray", "SeaGreen", "DeepSkyBlue", "LightSeaGreen", ]


# ------------------- #
# --- Challenge 1 --- #
# ------------------- #
def draw_square():
    """ Make the Turtle draw a square,
    """
    for _ in range(4):
        tim.forward(100)
        tim.left(90)


# draw_square()

# ------------------- #
# --- Challenge 2 --- #
# ------------------- #
def draw_dashed_line(number_of_times):
    """ Make the Turtle draw a dashed lines for a number of times.
    """
    for _ in range(number_of_times):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


# draw_dashed_line(200)


# ------------------- #
# --- Challenge 3 --- #
# ------------------- #
def draw_shape(number_of_sides):
    """ Drawing shapes from n number of sides
    """
    angle = 360 / number_of_sides
    print(f"Angle:\t {angle} \nNo.sides: \t {number_of_sides}")

    for i in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)


def draw_shape_n_sides(start_number, end_number):
    """ calls the draw_shape function to draw shapes with n number of sides.
    Increasing the number of sides for end_number.
    """
    for shape_side_n in range(start_number, end_number):
        draw_shape(shape_side_n)
        tim.color(choice(colors))


# draw_shape_n_sides(3, 200)


# ------------------- #
# --- Challenge 4 --- #
# ------------------- #
def random_color():
    """ Returns a random RGB Color in a tuple
    """
    t.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)

    return random_color


def random_walk(times):
    """ Random Walk the Turtle with bigger pen size and random colors.
    """
    directions = [0, 90, 180, 270]
    tim.speed(0)
    tim.pensize(8)

    for _ in range(times):
        tim.color(random_color())
        tim.forward(40)
        tim.setheading(choice(directions))


# random_walk(100)


# ------------------- #
# --- Challenge 5 --- #
# ------------------- #
def draw_circles(size_of_gap):
    """ Draws circles in a circle with random colors
    """
    tim.speed(0)
    for _ in range(int(360 / size_of_gap)):
        current_heading = tim.heading()
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(current_heading + size_of_gap)


# draw_circles(5)

# So the screen does not exit
screen = Screen()
screen.exitonclick()
