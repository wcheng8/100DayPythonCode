from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_hscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} | High Score: {self.hscore}",align="center", font = FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_hscore(self):
        with open('score.txt','r') as file:
            self.hscore = int(file.read())
        if self.score > self.hscore:
            self.hscore = self.score
            with open('score.txt','w') as file:
                file.write(str(self.hscore))

    def restart_game(self,snake):
        for segment in snake.snake:
            segment.goto(1000,1000)
        snake.snake = []
        snake.create_snake()
        self.update_hscore()
        self.clear()
        self.update_scoreboard()
        self.score = 0

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over :(", align="center", font = FONT)
        return True



