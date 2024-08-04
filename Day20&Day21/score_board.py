from turtle import Turtle
ALIGNING = "center"
FONT = ("Courier", 24, "normal")

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.write_the_score()
    
    def write_the_score(self):
        self.write(f"Score: {self.score}", align=ALIGNING, font=FONT)

    
    def increase_score(self):
        self.clear()
        self.score += 1 
        self.write_the_score()

    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNING, font=FONT)
        