from turtle import Turtle
from time import sleep

FONT = ("Courier", 18 , "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.goto(-175,270)
        self.score = 0
        self.color("black")
        self.write(f"Score : {self.score} ", align="center", font=FONT)


    def update_score(self):

        self.clear()
        self.goto(-175,270)
        self.write(f"Score : {self.score} ",align="center",font=FONT)

    def game_end(self):


        self.clear()
        self.goto(0,0)
        self.write("GAME OVER ", align="center", font=("Courier",50,"normal"))

    def show_level_up(self):

        self.goto(0, 0)
        self.write("LEVEL UP!", align="center", font=("Courier", 36, "bold"))
        sleep(0.5)
        self.clear()
