from turtle import Turtle

class state(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def draw_state(self,name,position):
        state_val = Turtle()
        state_val.penup()
        state_val.hideturtle()
        state_val.goto(position)
        state_val.write(name, align="center", font=("Arial", 10, "normal"))