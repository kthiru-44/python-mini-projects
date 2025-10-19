from turtle import Turtle
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270
POSITIONS = [(-20,0),(-40,0),(-60,0)]
class Snake():

    def __init__(self):

        self.new_turtle = None
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for position in POSITIONS:

            self.add_segment(position)


    def add_segment(self,position):
        self.new_turtle = Turtle("square")
        self.new_turtle.color("white")
        self.new_turtle.penup()
        self.new_turtle.goto(position)
        self.turtle_list.append(self.new_turtle)

    def extend(self):

        self.add_segment(self.turtle_list[-1].position())

    def move(self):

        for seg_num in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[seg_num - 1].xcor()
            new_y = self.turtle_list[seg_num - 1].ycor()
            self.turtle_list[seg_num].goto(new_x, new_y)

        self.head.forward(20)


    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):

        if self.head.heading() != LEFT:

            self.head.setheading(RIGHT)