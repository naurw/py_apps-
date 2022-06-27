
######################################
###### revising with high score ######
######################################

from turtle import Screen, Turtle 
import time 
from packages.snake import Snake 
from packages.food import Food 
from packages.scoreboard import Scoreboard

screen = Screen() 
screen.setup(width = 600, height = 600) 
screen.bgcolor('black') 
screen.title('Sneky Snek Turtles')
screen.tracer(0)
start = screen.textinput(title = 'Ready, Get Set, Go!', prompt= 'Are you ready to summon the turtle minions? (Type: Yes or No) ').lower()
is_on = False 

if start == 'yes':
    is_on = True 

snake = Snake() 
food = Food()
scoreboard = Scoreboard() 

screen.listen()
# interested in moving the first segment 
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

while is_on: 
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # detect collision with food using distance 
    if snake.head.distance(food) < 15: 
        food.refresh()
        snake.clones()
        scoreboard.increase_score()
    
    # detect collision with wall 
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280: 
        scoreboard.reset()

    # detect collision with tail 
    # use everything but the head using slicing (removed first if-statement)
    for minion in snake.minions[1:]: 
        if snake.head.distance(minion) < 10: 
            scoreboard.reset()



screen.exitonclick()