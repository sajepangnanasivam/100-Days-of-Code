from turtle import Turtle

FONT = ("Courier", 18, "bold")
ALIGNMENT = "left"


# TODO: (5) Add scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER!", font=("Courier", 22, "bold"), align="center")
