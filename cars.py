import turtle
from turtle import *
import random


colormode(255)


class Car():
    def __init__(self):
        self.cars = []
        self.move_dst=15

    def random_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.color(random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))
            car.shapesize(stretch_wid=1, stretch_len=random.randint(2,4))
            car.goto(380, random.randint(-225, 300))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.move_dst)

    def level_up(self):
        self.move_dst *= 1.3


