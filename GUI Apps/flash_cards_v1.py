from tkinter import * 
from PIL import ImageTk, Image
import pandas as pd 
import random

BG_COLOR = '#B1DDC6'
d = {} 

try: 
    df = pd.read_csv('/Users/William/Desktop/100_python_projects/100-Python-Projects-/random csv/words_to_learn.csv')
except FileNotFoundError: 
    original_df = pd.read_csv('/Users/William/Desktop/100_python_projects/100-Python-Projects-/random csv/french_words.csv')
    # turn nested dict to a list of dictioaries; useful for picking an entry 
    d = original_df.to_dict(orient = 'records')
else: 
    d = df.to_dict(orient = 'records')

card = {}

# ---------------------------- FLASH CARDS ------------------------------- #
def next_card(): 
    global card, timer 
    # cancel timer before next card; only after you are on the card does it initiate the flipping
    app.after_cancel(timer)
    card = random.choice(d)
    canvas.itemconfig(card_title, text = 'French', fill = 'black')
    canvas.itemconfig(card_word, text = card['French'], fill = 'black')
    canvas.itemconfig(card_background, image = card_front_img)
    timer = app.after(5000, func = flip_card)

def flip_card(): 
    canvas.itemconfig(card_title, text = 'English', fill = 'white')
    canvas.itemconfig(card_word, text = card['English'], fill = 'white')
    canvas.itemconfig(card_background, image = card_back_img)

def known_card(): 
    # removes the known cards and deck of flash card will decrease and will be saved in a new csv
    d.remove(card)
    print(len(d))

    # permanent storage of words to learn 
    df = pd.DataFrame(d)
    df.to_csv('random csv/words_to_learn.csv', index = False)

    next_card() 

# ---------------------------- UI SETUP ------------------------------- #
app = Tk() 
app.title('Flash Cards') 
app.config(padx = 50, pady = 50, bg = BG_COLOR)

# call the flipping of the card before the buttons 
timer = app.after(5000, func = flip_card)


canvas = Canvas(width=800, height=526, bg = BG_COLOR, highlightthickness= 0)
card_front_img = ImageTk.PhotoImage(Image.open("images/card_front.png"))
card_back_img = ImageTk.PhotoImage(Image.open("images/card_back.png"))
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text = 'Title', font = ('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text = 'Word', font = ('Arial', 60, 'bold'))
canvas.grid(column = 0, row = 0, columnspan=2)

# Buttons 
wrong_img = ImageTk.PhotoImage(Image.open("images/wrong.png"))
unknown_button = Button(image = wrong_img, highlightthickness= 0, highlightbackground= BG_COLOR, command = next_card)
unknown_button.grid(row=1, column = 0)

right_img = ImageTk.PhotoImage(Image.open("images/right.png"))
known_button = Button(image = right_img, highlightthickness= 0, highlightbackground= BG_COLOR, command = known_card)
known_button.grid(row=1, column = 1)

# initiate the flash cards 
next_card()

app.mainloop()
