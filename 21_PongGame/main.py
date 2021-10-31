import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
# 1. Create the Screen
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# 2. Create and move the paddle
# 3. Create another paddle
paddle_r = Paddle()
paddle_l = Paddle()
paddle_r.draw_paddle_r()
paddle_l.draw_paddle_l()

# 4. Create and move the ball

ball = Ball()
ball.draw_ball()
score = Score()
score.draw_scoreboard()

# 5. Detect collision with wall and bounce

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score

screen.exitonclick()