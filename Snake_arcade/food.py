from turtle import Turtle
import random
class Food(Turtle) :

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed(0)
        self.color("blue")
        self.refresh()

    def refresh(self):

        rx = random.randint(-250,250)
        ry = random.randint(-250,250)
        self.goto(rx,ry)
