import time
import cars
from cars import *
import player
from player import *
from scoreboard import *

my_screen=turtle.Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("gray")
my_screen.tracer(0)
player =Player()
car=Car()
scoreboard=Scoreboard()

my_screen.listen()
my_screen.onkey(player.go_up, 'Up')
game_on=True

while game_on:
    time.sleep(0.1)
    my_screen.update()
    car.random_cars()
    car.move()


    # cars and player collisiom
    for i in car.cars:
        if i.distance(player)<20:
            game_on=False
            scoreboard.game_over()

    if player.ycor()>300:
        player.create()
        scoreboard.increase_score()
        car.level_up()



my_screen.exitonclick()