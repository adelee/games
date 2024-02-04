import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(fun=player.move, key="Up")

car_manager = CarManager()
scoreboard = Scoreboard()

loop_number = 0
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if loop_number % 6 == 0:
        car_manager.add_car()
    car_manager.move()
    for car in car_manager.car_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() >= player.finish:
        player.restart()
        car_manager.increase_speed()
        scoreboard.increase_level()

    loop_number += 1


screen.exitonclick()
