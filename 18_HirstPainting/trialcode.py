from turtle import Turtle, Screen
from random import choice, randint
screen = Screen()
t = Turtle()
t.shape("turtle")
# Square
for i in range(4):
    t.forward(100)
    t.right(90)

# Dot line
for i in range(50):
    t.pencolor('black')
    t.forward(3)
    t.pencolor('white')
    t.forward(3)

# shapes
angles = [120,90,72,60,51.43,45,40,36]
colors = ['red','green','blue','orange','black']
for i in range(len(angles)):
    t.pencolor(choice(colors))
    for x in range(i+3):
        t.forward(100)
        t.right(angles[i])

# Random Walk

no_of_steps = 1000
colors = ['red','green','blue','orange','black']
for i in range(no_of_steps):
    t.right(randint(0,3)*90)
    t.pen(pencolor = choice(colors),speed = 7, pensize=10)
    t.forward(10)

def random_colors():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

# Spirograph
t.speed(20)
screen.colormode(255)
for i in range(72):
    t.pencolor(random_colors())
    t.circle(100)
    t.right(5)

screen.exitonclick()