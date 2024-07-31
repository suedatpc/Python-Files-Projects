from turtle import Turtle, Screen

tosbik = Turtle()
tosbik.shape("classic")


def move_forward():
    tosbik.forward(10)

def move_backward():
    tosbik.backward(10)

def left():
    new_heading = tosbik.heading() + 10
    tosbik.seth(new_heading)

def right():
    new_heading = tosbik.heading() - 10
    tosbik.seth(new_heading)

def clear():
    tosbik.clear()
    tosbik.penup()
    tosbik.home()
    tosbik.pendown()
    

screen = Screen()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(right, "d")
screen.onkey(left, "a")
screen.onkey(clear, "c")
screen.exitonclick()