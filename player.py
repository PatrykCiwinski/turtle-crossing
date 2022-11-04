import  turtle
from turtle import  *

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create()


    def create(self):
        self.shape("turtle")
        self.shapesize(stretch_wid=1.3)
        self.color("lime")
        self.penup()
        self.setheading(90)
        self.goto(0,-280)

    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

