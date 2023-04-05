from turtle import *


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("grey")
        self.shapesize(stretch_len=7)
        self.penup()
        self.goto(0, -280)


    def move_right(self):
        new_x = self.xcor() + 10
        if self.xcor() < 320:
            self.goto(new_x, self.ycor())


    def move_left(self):
        new_x = self.xcor() - 10
        if self.xcor() > -325:
            self.goto(new_x, self.ycor())