from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.movement = STARTING_MOVE_DISTANCE

    def add_car(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(260, random.randint(-250, 250))
        new_car.setheading(180)
        self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            if car.xcor() > -340:
                car.forward(self.movement)

    def increase_speed(self):
        self.movement += MOVE_INCREMENT
