from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

    def draw_ball(self):
        self.shape("turtle")
        self.color("white")