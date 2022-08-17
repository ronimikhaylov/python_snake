import random
from turtle import Screen, Turtle
from scoreboard import Scoreboard

class food():
    def __init__(self):
        self.food = Turtle(shape="circle")
        self.food.color("red")
        self.food.penup()
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food.speed("fastest")
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.food.goto(random_x, random_y)

    def get_coordinates(self):
        return self.food.position()
    def get_x(self):
        return self.food.xcor()