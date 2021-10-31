from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.positions = STARTING_POSITIONS
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in self.positions:
            segment = Turtle("square")
            segment.penup()
            segment.goto(position)
            segment.color("white")
            self.snake.append(segment)

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            x_front = self.snake[segment - 1].xcor()
            y_front = self.snake[segment - 1].ycor()
            self.snake[segment].goto(x_front, y_front)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake[0].heading() == 0 or self.snake[0].heading() == 180:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() == 0 or self.snake[0].heading() == 180:
            self.snake[0].setheading(270)

    def left(self):
        if self.snake[0].heading() == 90 or self.snake[0].heading() == 270:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading() == 90 or self.snake[0].heading() == 270:
            self.snake[0].setheading(0)