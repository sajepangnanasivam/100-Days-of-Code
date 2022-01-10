from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    """ Move the turtle forwards.
    """
    tim.forward(10)


def move_backwards():
    """ Move the turtle backwards.
    """
    tim.backward(10)


def turn_left():
    """ Turn the turtle left.
    """
    #tim.left(10)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    """ Turn the turtle right.
    """
    #tim.right(10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_screen():
    """ Clear the screen and move the turtle to home position.
    """
    tim.clear()
    tim.penup()
    tim.home() # tim.setposition(0, 0)
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
