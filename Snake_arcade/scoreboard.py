from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.write(arg=f"Score : {self.score}" , align="center",font=("Arial",15,"normal"))


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=("Arial",24,"normal"))


    def collide_food(self):

        self.score += 1
        self.clear()
        self.write(arg=f"Score : {self.score}" , align="center",font=("Arial",15,"normal"))

