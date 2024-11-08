from turtle import *
from player import *
from car_manager import *
from scoreboard import *
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up,"Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    #detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on =False
            scoreboard.game_over()

    #detect successful crossing
    if player.is_at_finish():
        player.start()
        car_manager.level_up()
        scoreboard.increase_level()

        

screen.exitonclick()