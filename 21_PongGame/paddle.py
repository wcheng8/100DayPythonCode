from turtle import Turtle
paddle_R = [(450,-40),(450,-20),(450,0),(450,20),(450,40)]
paddle_L = [(-450,-40),(-450,-20),(-450,0),(-450,20),(-450,40)]

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

    def draw_block(self,position):
        block = Turtle()
        block.shape("square")
        block.color("white")
        block.penup()
        block.goto(position)

    def draw_paddle_r(self):
        for position in paddle_R:
            self.draw_block(position)

    def draw_paddle_l(self):
        for position in paddle_L:
            self.draw_block(position)