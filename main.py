import time
from turtle import Screen

import car_manager
import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=800, height=800)
screen.tracer(0)
screen.listen()
cars = []
for _ in range(30):
    car = CarManager()
    cars.append(car)
p1 = Player()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(p1.up, "w")
    if p1.finish_line():
        score.increase_score()
        car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT
    for x in cars:
        x.move()
        if x.distance(p1) < 22:
            game_is_on = False
            score.game_over()







screen.exitonclick()
