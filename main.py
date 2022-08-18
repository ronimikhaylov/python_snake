import random
from turtle import Screen, Turtle
from snake import Snake
from food import food
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

snake = Snake()
fd = food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # if the coordinates of the snake and the food are off by 20, then the snake has eaten the food

    if snake.head.distance(fd.distance()) < 15:
        fd.refresh()
        snake.extend()
        scoreboard.update_scoreboard()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()