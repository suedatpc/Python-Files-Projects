import turtle
import pandas
from tkinter import messagebox

data = pandas.read_csv("Day25/day-25-us-states-game-start/50_states.csv")
state_list = data.state.to_list()

guessed_states = []

t = turtle.Turtle()
t.hideturtle()
t.penup()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day25/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"State {len(guessed_states)}/50", prompt="Enter a state name:").title()
    
    if answer_state in state_list:
        guessed_states.append(answer_state)

        index = state_list.index(answer_state)
        x_cor = data.iloc[index, 1]
        y_cor = data.iloc[index, 2]
        
        t.goto(x_cor, y_cor)
        t.write(answer_state , align="left")

        del state_list[index]
    
    elif answer_state in guessed_states:
        messagebox.showinfo(title="Try Again", message=f"{answer_state} is already guessed and on the map")
    
    else:
        messagebox.showinfo(title="Incorrect Guess", message=f"{answer_state} is not on the map")

if len(guessed_states) == 50:
    messagebox.showinfo(title="Full Map", message="No more guesses left.")    