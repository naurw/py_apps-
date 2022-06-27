from turtle import Turtle 

STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20 
UP = 90 
DOWN = 270 
LEFT = 180 
RIGHT = 0


class Snake: 

    def __init__(self):
        self.minions = [] 
        self.create_snake() 
        self.head = self.minions[0]
    
    def create_snake(self):  
        for pos in STARTING_POS: 
           self.add_clones(pos)

    def clones(self): 
        self.add_clones(self.minions[-1].position())

    def add_clones(self, pos): 
        turtle_train = Turtle('turtle')
        turtle_train.color('white')
        turtle_train.penup()
        turtle_train.goto(pos)
        self.minions.append(turtle_train)

    def reset(self):
        for minion in self.minions: 
            minion.goto(1000,1000)
        self.minions.clear() 
        self.create_snake() 
        self.head = self.minions[0]

    def move(self): 
        for seg_num in range(len(self.minions)-1, 0, -1):
            new_x = self.minions[seg_num-1].xcor()
            new_y = self.minions[seg_num-1].ycor()
            self.minions[seg_num].goto(new_x, new_y) 
        self.head.forward(MOVE_DISTANCE)

    def up(self): 
        if self.head.heading() != DOWN: 
            self.head.setheading(UP)

    def down(self): 
        if self.head.heading() != UP: 
            self.head.setheading(DOWN)        
    
    def left(self): 
        if self.head.heading() != RIGHT: 
            self.head.setheading(LEFT)

    def right(self): 
        if self.head.heading() != LEFT: 
            self.head.setheading(RIGHT) 
