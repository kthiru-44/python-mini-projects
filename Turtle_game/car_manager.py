import turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


from turtle import *

import random



class CarManager():

    def __init__(self):

        self.car_list = []

    def create_car(self):

        chance = random.randint(1,6)
        if chance == 6 :
            new_car =  Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            coord = (300,random.randint(-270,270))
            new_car.goto(coord)
            self.car_list.append(new_car)


    def move(self):

        for car in self.car_list :

            car.backward(MOVE_INCREMENT)


    def reset_level(self):

        for car in self.car_list :
            car.hideturtle()
            car.clear()


        self.car_list = []

    def game_over(self,x,y):

        for car in self.car_list :

            if car.distance(x,y) < 25 :

                return True

            else :
                pass









