from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, shape: str = "circle"):
        super().__init__(shape)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) 
        self.color("blue")
        self.speed("fastest")
        self.food_location()

    
    def food_location(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)