STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.speed(0)

    def move(self):

        self.forward(MOVE_DISTANCE)


    def reset_pos(self):

        self.goto(STARTING_POSITION)
        self.setheading(90)


