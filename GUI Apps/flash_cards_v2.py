from tkinter import * 
from PIL import ImageTk, Image
import pandas as pd 
import random
import playsound
from gtts import gTTS
import os 

os.getcwd()
BG_COLOR = '#B1DDC6'
current_card = {}
unknown_words = {}

try: 
    new_df = pd.read_csv('random csv/words_to_learn.csv')
except FileNotFoundError: 
    original_df = pd.read_csv('random csv/french_words.csv')
    # turn nested dict to a list of dictionaries to make it easier pick out an entry from within
    d = original_df.to_dict(orient = 'records')
else: 
    d = new_df.to_dict(orient = 'records')


# ---------------------------- FLASH CARDS w. TEXT-TO-SPEECH ------------------------------- #
def next_card():
    global current_card, timer 
    language = 'fr' 
    current_card = random.choice(d)
    # cancel timer before next card; only after you are on the card does it initiate the flipping
    app.after_cancel(timer)
    canvas.itemconfig(card_title, text = 'French', fill = 'black')
    canvas.itemconfig(card_word, text = current_card['French'], fill = 'black')
    canvas.itemconfig(card_background, image = card_front_img)
    app.after(100)
    audio_output = gTTS(text=current_card["French"], lang=language)
    audio_output.save("flash_card_audio/english_word.mp3")
    playsound.playsound("flash_card_audio/english_word.mp3", True)
    os.remove("flash_card_audio/english_word.mp3")
    timer = app.after(5000, func = flip_card)

def flip_card(): 
    language = 'en'
    canvas.itemconfig(card_title, text = 'English', fill = 'white')
    canvas.itemconfig(card_word, text = current_card['English'], fill = 'white')
    canvas.itemconfig(card_background, image = card_back_img)
    audio_output = gTTS(text=current_card["English"], lang=language)
    audio_output.save("flash_card_audio/french_word.mp3")
    playsound.playsound("flash_card_audio/french_word.mp3", True)
    os.remove("flash_card_audio/french_word.mp3")

def known_card(): 
    # removes the known cards and deck of flash card will decrease and will be saved in a new csv
    d.remove(current_card)
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
