from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.safeheight = 250
        self.setheading(180)
        self.cars = []
        self.hideturtle()

    def draw_car(self):
        car = Turtle()
        car.shape("turtle")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=1.5)
        car.color(random.choice(COLORS))
        car.goto(300, random.randint(-self.safeheight, self.safeheight))
        self.cars.append(car)

    def move_car(self,car, score):
        car.setheading(180)
        car.forward(STARTING_MOVE_DISTANCE + score.level * MOVE_INCREMENT)