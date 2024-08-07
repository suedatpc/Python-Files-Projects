from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.write_score()
        
    
    def write_score(self):
        self.setpos(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.setpos(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    
    def increase_left_score(self):
        self.clear()
        self.left_score += 1
        self.write_score()

    def increase_right_score(self):
        self.clear()
        self.right_score += 1
        self.write_score()