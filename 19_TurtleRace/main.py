from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
screen.setup(width=500, height=400)
colors = ['red','orange','yellow','green','blue','purple']

# TODO 1: Positioning the turtle to start
# Create different instances
turtles = []
for x in range(6):
    turtle = Turtle()
    turtles.append(turtle)

index = 0

for turtle in turtles:
    turtle.penup()
    turtle.shape("turtle")
    turtle.color(colors[index])
    index+=1
    turtle.goto(x = -230, y = -150+(index*50))

bet = screen.textinput(title="Make your bet", prompt=f'Select the turtle color that will win!')

# TODO 2: Make turtle reach the finish line
finished = False

while(not finished):
    for turtle in turtles:
        turtle.forward(randint(1,10))
        if turtle.xcor() >= 230:
            winner = turtle.ycor()
            # print(winner)
            finished = True

win_color = (colors[int((winner+150)/50)-1])

# TODO 3: Determine which turtle won and present the winner and see if it matches your guess

if win_color == bet:
    print("You won your bet! Your prize is pride!")
else:
    print(f"The winner was {win_color} :(. Better luck next time!")

screen.exitonclick()
