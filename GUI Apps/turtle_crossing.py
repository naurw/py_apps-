#############################
###### Turtle Crossing ######
#############################

# 5 steps: 
# move the turtle with keypress
# create and move the cars 
# detect collision with car 
# detect when turtle reaches the other side 
# create a scoreboard 

from turtle import Screen
import time 
from packages.player import Player 
from packages.car_manager import CarManager 
from packages.turtle_crossing_scoreboard import Scoreboard 


screen = Screen() 
screen.title('Turtle Crossing')
screen.setup(width = 600, height = 600)
screen.tracer(0)


player = Player() 
car_manager = CarManager() 
scoreboard = Scoreboard()

screen.listen() 
screen.onkey(player.up, 'Up')


is_on = True 
while is_on: 
    time.sleep(0.1)
    screen.update() 

    car_manager.create_car() 
    car_manager.move_cars() 

    # detect collision with car 
    for car in car_manager.all_cars: 
        if car.distance(player) < 20: 
            is_on = False 
            scoreboard.game_over() 

    # detect successful crossing 
    if player.is_at_finish_line(): 
        player.restart() 
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick() 