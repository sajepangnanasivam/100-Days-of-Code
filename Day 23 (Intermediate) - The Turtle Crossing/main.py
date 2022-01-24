import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # TODO: (3) Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # TODO: (4) Detect when player has reachead goal
    if player.is_at_finish_line():
        scoreboard.increase_score()
        player.goto_start_position()
        car_manager.level_up()


screen.exitonclick()

