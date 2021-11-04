from turtle import Turtle, Screen
import pandas as pd
from name import state
screen_turtle = Turtle()
screen = Screen()
screen.title("US States")
screen.addshape("blank_states_img.gif")
screen_turtle.shape("blank_states_img.gif")

correct_states = []
state_card = state()
states_df = pd.read_csv("50_states.csv")
states_name = states_df.state.to_list()
state_length = len(states_name)
x_pos = states_df.x.to_list()
y_pos = states_df.y.to_list()
positions = []
for i in range(state_length):
    positions.append((x_pos[i], y_pos[i]))

game_on = True
while game_on:
    guess = screen.textinput(title=f"({len(correct_states)}/50) Guess the state", prompt="Guess a states name.")

    for i in range(state_length):
        if guess.lower() == states_name[i].lower():
            state_card.draw_state(states_name[i], positions[i])
            correct_states.append(states_name[i])

    if len(correct_states) == 3:
        screen_turtle.write("You finished the game!", align="center", font = ("Arial", 24, "normal"))
        game_on = False

    if guess == "exit":
        screen_turtle.write("Check the states you missed in the csv :( Better luck next time!", align="center", font = ("Arial", 24, "normal"))
        for state in correct_states:
            states_name.remove(state)
        needs_practice_df = pd.DataFrame({"States": states_name})
        needs_practice_df.to_csv("Practice_States.csv")
        game_on = False


screen.exitonclick()