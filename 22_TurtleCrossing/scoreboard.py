from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.score = 0
        self.penup()
        self.hideturtle()

    def level_up(self):
        self.clear()
        self.level += 1

    def score_board(self):
        self.goto(-230,240)
        self.write(f"Level: {self.level}\nScore: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.write("Game over!", align="center", font = FONT)
