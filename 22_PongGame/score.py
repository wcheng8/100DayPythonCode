from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = [0,0]
        self.hideturtle()

    def draw_scoreboard(self):
        self.goto(-10,260)
        self.write(f"Score: {self.score[0]} | {self.score[1]}", align="center", font = ("Courier", 24, "normal"))

    def restart_screen(self):
        self.goto(0,0)
        self.write("Press Space to continue", align="center", font = ("Courier", 24, "normal"))

    def increment_score(self,winner):
        if winner == "Right":
            self.score[0] += 1
            self.clear()
            self.draw_scoreboard()
        else:
            self.score[1] += 1
            self.clear()
            self.draw_scoreboard()

    def quit_game(self):
        self.score = [10,10]

    def check_score(self):
        if self.score[0] == 1 or self.score[1] == 10:
            return True