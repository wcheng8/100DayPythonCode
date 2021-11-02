import time
from turtle import Screen
from player import Player
from Collision import Collision
from car_manager import CarManager
from scoreboard import Scoreboard
from food import food

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player on screen and make it move
player = Player()
player.draw_player()
# Create boundary
boundary = Collision()
cars = CarManager()
# Create collision with player feature
# Create scoreboard
score = Scoreboard()
game_over = Scoreboard()
food_available = food()
# Create gamelevels (increment gamespeed subsequent level)
# Create gameover screen
index = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    boundary.check_boundary(player)
    score.score_board()
    screen.onkeypress(player.move_forward,"Up")
    screen.onkeypress(player.move_back,"Down")
    screen.onkeypress(player.move_right,"Right")
    screen.onkeypress(player.move_left,"Left")
    if index == 0 or index%15 == 0:
        food_available.create_food()
    if index%6 == 0:
        cars.draw_car()
    for food in food_available.food_arr:
        if player.distance(food) <= 10:
            score.clear()
            score.score += 1
            food_available.food_arr.remove(food)
            food.hideturtle()
    for car in cars.cars:
        cars.move_car(car,score)
        if player.distance(car) <= 20:
            game_over.game_over()
            game_is_on = False
    if boundary.win_condition1(player):
        score.level_up()
        for food in food_available.food_arr:
            food.hideturtle()
    index+=1
    screen.listen()


screen.exitonclick()