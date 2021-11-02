from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
TESTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0),(-60, 0),(-80, 0),(-100, 0),(-120, 0)]


class Snake:
    def __init__(self):
        self.positions = TESTING_POSITIONS
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in self.positions:
            self.add_snake_segment(position)

    def add_snake_segment(self,position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
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

    def grow_snake(self):
        end_position = self.snake[-1].pos()
        self.add_snake_segment(end_position)

    def check_boundary(self):
        x_pos = self.snake[0].xcor()
        y_pos = self.snake[0].ycor()
        if x_pos >= 300 or x_pos <= -300 or y_pos >= 300 or y_pos <= -300:
            return True
        return False

