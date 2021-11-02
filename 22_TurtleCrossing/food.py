from turtle import Turtle
import random


class food(Turtle):
    def __init__(self):
        super().__init__()
        self.food_arr = []

    def create_food(self):
        new_food = Turtle()
        new_food.shape("circle")
        new_food.penup()
        new_food.color("red")
        y_pos = random.randint(-250,250)
        x_pos = random.randint(-250,250)
        new_food.goto(x_pos, y_pos)
        self.food_arr.append(new_food)

    def clear_food(self):
        self.clear()
        self.reset()
        self.food_arr = []
