from turtle import Turtle, Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard
import time 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

#Detect collision with cars
    for carr in car.car_list:
        if player.distance(carr) < 20:
            game_is_on = False
            scoreboard.game_over()
#lvl up 
    if player.is_at_finish_line():
        player.go_to_start()
        car.speed_up()
        scoreboard.increase_level()



screen.exitonclick()