from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-10,260)
        self.score = 0
        self.hideturtle()

    def draw_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font = ("Courier", 24, "normal"))
