from turtle import Turtle
paddle_R = [(450,-40),(450,-20),(450,0),(450,20),(450,40)]
paddle_L = [(-450,-40),(-450,-20),(-450,0),(-450,20),(-450,40)]

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

    def draw_paddle_r(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(450,0)

    def draw_paddle_l(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(-450,0)


    def mup(self):
        self.goto(self.xcor(), self.ycor()+20)

    def mdown(self):
        self.goto(self.xcor(), self.ycor()-20)
