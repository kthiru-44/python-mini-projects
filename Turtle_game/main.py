import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import winsound  # Only on Windows

def play_level_up_sound():
    winsound.Beep(800, 200)  # frequency, duration in ms


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
speed = 0.2

scoreboard = Scoreboard()

p1 = Player()
screen.onkey(p1.move,"Up")


car = CarManager()



game_is_on = True

while game_is_on:

    time.sleep(speed)
    screen.update()
    x1 = p1.xcor()
    y1 = p1.ycor()

    car.create_car()
    car.move()


    if p1.ycor() >= 280 :

        scoreboard.score += 1
        car.reset_level()
        play_level_up_sound()
        speed *= 0.9
        p1.reset_pos()
        scoreboard.show_level_up()
        scoreboard.update_score()


    elif car.game_over(x1,y1) :

        scoreboard.game_end()
        game_is_on = False



screen.mainloop()

