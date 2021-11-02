from turtle import Turtle
from random import choice

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_vel = 10
        self.y_vel = 10
        self.x_cor = self.xcor()
        self.y_cor = self.ycor()
        self.penup()

    def draw_ball(self):
        self.shape("turtle")
        self.color("white")

    def move(self):
        self.x_cor += self.x_vel
        self.y_cor += self.y_vel
        self.goto(self.x_cor, self.y_cor)

    def reset(self):
        self.x_cor = 0
        self.y_cor = 0
        self.x_vel = 0
        self.y_vel = 0

    def start(self):
        self.x_vel = 10 * choice([-1,1])
        self.y_vel = 10 * choice([-1,1])
        return True


