import time
from score import ScoreBoard
from Snake import Snake
from turtle import Screen
from food import Food

screen = Screen()
screen.setup(height = 600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

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
    if snake.snake[0].distance(food) <= 15:
        food.refresh()
        score.add_score()
        snake.grow_snake()

# TODO 4: Detect collision with food

    if snake.check_boundary():
        score.game_over()
        game_on = False

    for segment in snake.snake[1:]:
        if snake.snake[0].distance(segment) < 10:
            score.game_over()
            game_on = False


# TODO 7: Detect collision with tail

screen.exitonclick()