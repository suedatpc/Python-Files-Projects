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
        with open("updated_snake_game/data.txt") as data:
            self.high_score = int(data.read())
        self.write_the_score()
    
    def write_the_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNING, font=FONT)

    
    def increase_score(self):
        self.score += 1 
        self.write_the_score()


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("updated_snake_game/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.write_the_score()