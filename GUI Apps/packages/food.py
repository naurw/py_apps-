from turtle import Turtle 
import random 

# can define food using the turtle package one by one 
# ALTERNATIVELY simply INHERIT from the Turtle class to skip some steps 

class Food(Turtle): 

    def __init__(self): 
        super().__init__() 
        self.shape('circle')
        self.penup() 
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color('blue') 
        self.speed('fastest')
        self.refresh()

    def refresh(self): 
        ran_x = random.randint(-280, 280)
        ran_y = random.randint(-280, 280)
        self.goto(ran_x, ran_y)
