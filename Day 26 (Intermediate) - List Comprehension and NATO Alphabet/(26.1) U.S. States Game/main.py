import pandas as pd
import turtle

# Setting up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=750, height=500)

# Adding the image on screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Getting the dataset
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# TODO: (4) Use a loop the allow the user to keep guessing
while len(guessed_states) < 50:
    # TODO: (1) Get user input and convert the guess to title case
    # TODO: (6) Keep a track of the score
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                   prompt="Name a state").title()

    # TODO: (2) Check if the guess is among the 50 states
    if user_answer == "Exit":
        # Using List comprehension
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if user_answer in all_states:
        if user_answer not in guessed_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            # TODO: (3) Write correct guesses onto the map
            state_data = data[data.state == user_answer]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(state_data.state.item())
            # TODO: (5) Record the correct guesses in a list
            guessed_states.append(user_answer)
            print(guessed_states)
