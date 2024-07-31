from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

starting_x = -230
starting_y = -100
is_racing = False

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[index])
    new_turtle.penup()
    new_turtle.goto(starting_x, starting_y)
    starting_y += 35
    all_turtles.append(new_turtle)


if user_bet:
    is_racing = True


while is_racing:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)

        if turtle.xcor() > 220:
            is_racing = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")



screen.exitonclick()