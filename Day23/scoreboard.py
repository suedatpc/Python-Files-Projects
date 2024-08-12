from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.setpos(-250, 255)
        self.write_level()
    
    def write_level(self):
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write_level()

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
