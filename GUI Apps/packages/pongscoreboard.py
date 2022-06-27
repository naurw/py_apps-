from turtle import Turtle 
POS = 'center' 
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle): 

    def __init__(self):
        super().__init__()
        self.score = 0 
        self.color('white')
        self.penup()
        self.hideturtle() 
        self.l_score = 0
        self.r_score = 0

    def update(self): 
        self.clear()
        self.goto(-100,200)
        self.write(f'Left: {self.l_score}', align = POS, font = FONT)
        self.goto(100,200)
        self.write(f'Right: {self.r_score}', align = POS, font = FONT)

    def l_point(self): 
        self.l_score += 1
        self.update() 

    def r_point(self): 
        self.r_score += 1
        self.update() 
 

