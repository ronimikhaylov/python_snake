

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
       # self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        
    def update_scoreboard(self):
        self.score += 1
        if (self.score >= self.high_score):
            self.high_score = self.score
        self.clear()
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.clear()
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.goto(0, 270)
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))