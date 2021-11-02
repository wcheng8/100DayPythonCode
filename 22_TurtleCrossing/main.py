import time
from turtle import Screen
from player import Player
from Collision import collision
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player on screen and make it move
player = Player()
player.draw_player()
# Create boundary
boundary = collision()
cars = CarManager()
# Create collision with player feature
# Create scoreboard
score = Scoreboard()
game_over = Scoreboard()
# Create gamelevels (increment gamespeed subsequent level)
# Create gameover screen
index = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    boundary.check_boundary(player,score)
    score.score_board()
    screen.onkeypress(player.move_forward,"Up")
    screen.onkeypress(player.move_back,"Down")
    screen.onkeypress(player.move_right,"Right")
    screen.onkeypress(player.move_left,"Left")
    if index%6 == 0:
        cars.draw_car()
    for car in cars.cars:
        cars.move_car(car,score)
        if player.distance(car) <= 20:
            game_over.game_over()
            game_is_on = False
    index+=1
    screen.listen()


screen.exitonclick()