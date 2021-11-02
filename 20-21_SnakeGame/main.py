# with open('score.txt', 'r') as file:
#     lines = file.read()
#
# print(type(lines))
import time
from score import ScoreBoard
from Snake import Snake
from turtle import Screen, Turtle
from food import Food

FONT = ("Courier", 24, "normal")

screen = Screen()
screen.setup(height = 600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

global game_on
game_on = True
def game_over():
    game_screen = Turtle()
    game_screen.goto(0, 0)
    game_screen.write("Game Over :(", align="center", font=FONT)
    game_on = False

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")
    # screen.onkey(game_over,"q")
    if snake.snake[0].distance(food) <= 15:
        food.refresh()
        score.add_score()
        snake.grow_snake()

# TODO 4: Detect collision with food

    if snake.check_boundary():
        score.restart_game(snake)

    for segment in snake.snake[1:]:
        if snake.snake[0].distance(segment) < 10:
            score.restart_game(snake)

# TODO 7: Detect collision with tail


screen.exitonclick()