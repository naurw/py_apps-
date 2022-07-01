# ------- Kanye Quotes -------- # 
from tkinter import *
from PIL import ImageTk, Image
import requests 
import os 

os.chdir('/Users/William/Desktop/100_python_projects/100-Python-Projects-')
os.getcwd()

def get_quote():
    response = requests.get('https://api.kanye.rest')
    response.raise_for_status()
    data = response.json()
    quote = data['quote']
    print(quote)
    canvas.itemconfig(quote_text, text = quote)


get_quote()


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
img = ImageTk.PhotoImage(Image.open("kanye/background.png"))
canvas.create_image(150, 207, image=img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()