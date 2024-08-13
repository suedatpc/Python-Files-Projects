from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score_board import Score_board

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score_board()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#Detect collision with food 
    if snake.segments[0].distance(food) < 15:
        food.food_location()
        snake.extend()
        score_board.increase_score()


#Detect collision with wall
    if snake.segments[0].xcor() > 285 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -285:
        score_board.reset_score()
        snake.reset_snake()

#Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            score_board.reset_score()
            snake.reset_snake()

screen.exitonclick()
