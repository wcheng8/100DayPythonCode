from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.x_vel = 10
        self.y_vel = 10
        self.penup()
        self.setheading(90)
        self.goto(0,-280)

    def draw_player(self):
        self.shape("turtle")
        self.color("Green")

    def move_forward(self):
        new_x = self.xcor()
        new_y = self.ycor() + self.y_vel
        self.goto(new_x,new_y)
    def move_right(self):
        new_x = self.xcor() + self.x_vel
        new_y = self.ycor()
        self.goto(new_x,new_y)
    def move_left(self):
        new_x = self.xcor() - self.x_vel
        new_y = self.ycor()
        self.goto(new_x,new_y)
    def move_back(self):
        new_x = self.xcor()
        new_y = self.ycor() - self.y_vel
        self.goto(new_x,new_y)