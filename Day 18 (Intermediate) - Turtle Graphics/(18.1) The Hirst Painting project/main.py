import turtle

import colorgram
from colorgram.colorgram import Rgb
from turtle import Turtle, Screen
from random import choice

color_list = [Rgb(r=202, g=164, b=109), Rgb(r=238, g=240, b=245), Rgb(r=150, g=75, b=49), Rgb(r=223, g=201, b=135),
              Rgb(r=52, g=93, b=124), Rgb(r=172, g=154, b=40), Rgb(r=140, g=30, b=19), Rgb(r=133, g=163, b=185),
              Rgb(r=198, g=91, b=71), Rgb(r=46, g=122, b=86), Rgb(r=72, g=43, b=35), Rgb(r=145, g=178, b=148),
              Rgb(r=13, g=99, b=71), Rgb(r=233, g=175, b=164), Rgb(r=161, g=142, b=158), Rgb(r=105, g=74, b=77),
              Rgb(r=55, g=46, b=50), Rgb(r=183, g=205, b=171), Rgb(r=36, g=60, b=74), Rgb(r=18, g=86, b=90),
              Rgb(r=81, g=148, b=129), Rgb(r=148, g=17, b=20), Rgb(r=14, g=70, b=64), Rgb(r=30, g=68, b=100),
              Rgb(r=107, g=127, b=153), Rgb(r=174, g=94, b=97), Rgb(r=176, g=192, b=209)]


def get_colors_from_image():
    """ Using the colorgram module to extract 30 colors from image source
    """
    rgb_colors = []
    colors = colorgram.extract("image.jpg", 30)
    for color in colors:
        rgb_colors.append(color.rgb)
    return rgb_colors


def initialize_turtle():
    """ Initializing the turtle with speed, pensize, colormode, and position
    """
    tim = Turtle()
    tim.speed(0)
    tim.pensize(15)
    tim.setposition(0, 0)
    turtle.colormode(255)
    return tim


def get_random_color():
    """ Get a random color from the list
    """
    r_color = choice(color_list)
    return r_color


def draw_spots_horizontally(rows, columns, dotsize, gap):
    """ Draws Hirst painting

        rows (int):     Number of rows with dots
        columns (int):  Number of columns with dots
        dotsize (int):  Size of the dot
        gap (int):      Size of the gap between the dots
    """
    tim = initialize_turtle()
    row_count, x_cord, y_cord = 0, 0, 0
    while row_count != rows:
        for _ in range(columns):
            random_color = get_random_color()
            tim.dot(dotsize, random_color)
            tim.penup()
            tim.forward(gap)
        row_count += 1
        y_cord += gap
        print(row_count)
        tim.setposition(x_cord, y_cord)


draw_spots_horizontally(rows=10, columns=10, dotsize=25, gap=50)

screen = Screen()
screen.exitonclick()
