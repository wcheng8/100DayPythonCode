import time
from Snake import Snake
from turtle import Turtle, Screen


screen = Screen()
screen.setup(height = 600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# TODO 1: Create the snake body

snake = Snake()

# TODO 2: Move the snake
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")

# TODO 3: Create snake food
# TODO 4: Detect collision with food
# TODO 5: Create a scoreboard
# TODO 6: Detect collision with wall
# TODO 7: Detect collision with tail

screen.exitonclick()