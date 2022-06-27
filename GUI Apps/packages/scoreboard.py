from turtle import Turtle 
POS = 'center' 
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle): 

    def __init__(self):
        super().__init__()
        self.score = 0 
        with open('snake.txt') as f: 
            self.high_score = int(f.read())
        self.color('white')
        self.penup()
        self.goto(x= 0, y = 270)
        self.hideturtle() 
        self.update()

    def update(self): 
        self.clear() 
        self.write(f'NOM NOM NOM: {self.score} Highest Score: {self.high_score}', align = POS, font = FONT)
    
    # def game_over(self): 
    #     self.goto(0,0)
    #     self.write('GAME OVER 🤬', align = POS, font = FONT)

    def reset(self): 
        if self.score > self.high_score: 
            self.high_score = self.score 
            with open('snake.txt', 'w') as f: 
                f.write(f'{self.high_score}')
        self.score = 0 
        self.update()


    def increase_score(self): 
        self.score += 1 
        self.update() 
        