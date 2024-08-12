from turtle import Turtle
import random

COLORS = ["tomato1", "LightSalmon1", "LightGoldenrodYellow", "thistle1", "LightBlue1", "SlateBlue2"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car:
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_list = []
        

    def create_car(self):
        if random.randint(0, 15) % 5 == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setpos(300, random.randint(-250, 250))
            self.car_list.append(new_car)


    def move_cars(self):
        for car in self.car_list:
            car.backward(self.car_speed)
            if car.xcor() < -320:  # Remove car if it moves off the screen
                car.hideturtle()
                self.car_list.remove(car)
        
    
    def speed_up(self):
        self.car_speed += MOVE_INCREMENT