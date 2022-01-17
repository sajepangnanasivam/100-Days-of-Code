from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # 10 x 10 circle
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("crimson")
        self.speed("fastest")

        self.refresh()

    def refresh(self):
        random_x, random_y = random.randint(-280, 280), random.randint(-280, 280)
        self.goto(random_x, random_y)