from turtle import Turtle

class Collision(Turtle):
    def __init__(self):
        super().__init__()

    def detect_wall(self, ball):
        if ball.ycor() > 270 or ball.ycor() < -270:
            ball.y_vel = -ball.y_vel

    def detect_paddle(self,ball, paddle):
        if ball.distance(paddle) <= 15:
            ball.x_vel = -ball.x_vel

    def round_winner(self, ball):
        if ball.xcor() > 470:
            ball.reset()
            return "Right"
        if ball.xcor() < -470:
            ball.reset()
            return "Left"
