from turtle import *
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")


while game_on :

    screen.update()
    time.sleep(0.2)

    snake.move()

    if snake.head.distance(food) < 14 :
        food.refresh()
        scoreboard.collide_food()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() <  -290 :
        game_on = False
        scoreboard.game_over()

    for segment in snake.turtle_list[1:] :

        if snake.head.distance(segment) < 10 :
            game_on = False
            scoreboard.game_over()














































screen.exitonclick()