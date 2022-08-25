import random
from turtle import Screen, Turtle
from scoreboard import Scoreboard

class food(Turtle):
    
    def __init__(self):
        #super().__init__()
        self.food = Turtle()
        self.food.shape("circle")
        self.food.penup()
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)          
        self.food.color("red")
        self.food.speed("fastest")
        

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.food.goto(random_x, random_y)
        
    def distance(self):
        x1 = self.food.xcor()
        y1 = self.food.ycor()
        return x1, y1
    