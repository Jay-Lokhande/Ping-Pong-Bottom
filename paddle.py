import turtle
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("#C7F55B")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)


    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def size_small(self):
        size = self.turtlesize()
        increase = tuple([0.5 * num for num in size])
        self.turtlesize(*increase)

    def size_big(self):
        size = self.turtlesize()
        increase = tuple([1.5 * num for num in size])
        self.turtlesize(*increase)