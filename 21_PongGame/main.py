import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from collision import Collision
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
status = Score()
score.draw_scoreboard()
collision_detect = Collision()

# 5. Detect collision with wall and bounce

game_on = True
def clear_startball():
    ball.start()
    status.clear()

while game_on:
    screen.update()
    time.sleep(0.1)
    collision_detect.detect_wall(ball)
    screen.listen()
    screen.onkeypress(paddle_r.mup,"Up")
    screen.onkeypress(paddle_r.mdown,"Down")
    screen.onkeypress(paddle_l.mup, "w")
    screen.onkeypress(paddle_l.mdown,"s")
    screen.onkeypress(score.quit_game,"q")
    collision_detect.detect_paddle(ball, paddle_r)
    collision_detect.detect_paddle(ball, paddle_l)
    screen.onkeypress(clear_startball,"space")
    winner = collision_detect.round_winner(ball)
    if winner == "Right" or winner == "Left":
        score.increment_score(winner)
        status.restart_screen()

    ball.move()
    if score.check_score():
        game_on = False

status.clear()
status.write("We have a Winner!", align="center", font=("Courier", 24, "normal"))

screen.exitonclick()