#hirst_painting

import turtle as t
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.speed("fastest")
timmy_the_turtle.pensize(10)
t.colormode(255)


color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

timmy_the_turtle.hideturtle()
timmy_the_turtle.penup()
timmy_the_turtle.setheading(135)
timmy_the_turtle.fd(350)
timmy_the_turtle.seth(0)
number_of_dots = 100

for dots in range(1, number_of_dots + 1): 
    timmy_the_turtle.dot(20, random.choice(color_list))
    timmy_the_turtle.fd(50)
    if dots % 10 == 0:
        timmy_the_turtle.seth(270)
        timmy_the_turtle.fd(50)
        timmy_the_turtle.seth(180)
        timmy_the_turtle.fd(500)
        timmy_the_turtle.seth(0)



screen = Screen()
screen.exitonclick()