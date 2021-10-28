###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
from turtle import Turtle, Screen
from random import choice
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

# print(colors)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))


rgb_colors = rgb_colors[3:]
print(rgb_colors)

screen = Screen()
t = Turtle()

def drawdot():
    t.dot(20,choice(rgb_colors))
# Set origin and screen size
screen.colormode(255)
# Hide pen and turtle
t.hideturtle()
t.penup()

# Set cursor to lower left of screen
t.right(140)
t.forward(300)
t.left(140)

# Draw dots
for y in range(10):
    for x in range(10):
        drawdot()
        t.forward(50)
    # Go to next row
    t.left(175)
    t.forward(502)
    t.right(175)

screen.exitonclick()