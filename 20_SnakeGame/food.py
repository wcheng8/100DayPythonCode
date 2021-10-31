from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.goto(randint(-280,280),randint(-280,280))

    def refresh(self):
        self.goto(randint(-280,280),randint(-280,280))
