
from email import message
from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk, Image
import random 
import pyperclip 
import json

YELLOW = "#f7f5dd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password) 
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(): 

    dict = {
        website_entry.get() : {
            'email' : email_entry.get(),
            'password' : password_entry.get()
        } 
    }

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0: 
        messagebox.showinfo(title = 'Error', message = "Please make sure you don't have any empty fields.")
    
    # instead of a txt, create a json to be able to read through like a dictionary 
    else: 
        try: 
            with open('password generator/data.json', 'r') as f: 
                # reading old data
                data = json.load(f)
        except FileNotFoundError: 
            with open('password generator/data.json', 'w') as f: 
                # creating json file if doens't exist 
                json.dump(dict, f, indent = 4)
        else: 
            # updating old data with new data 
            data.update(dict)

            with open('password generator/data.json', 'w') as f: 
                # saving updated data once try statement passes / updates dict 
                json.dump(data, f, indent = 4)
        finally: 
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password(): 
    website = website_entry.get() 
    try: 
        with open('password generator/data.json', 'r') as f: 
            data = json.load(f)
    except FileNotFoundError: 
        messagebox.showinfo(title = 'Error', message = 'Data Not Found.')
    else: 
        if website in data: 
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title = website, message = f'Email: {email}\nPassword: {password}')
        else: 
            messagebox.showinfo(title = 'Error', message = f'There are no credentials stored for {website}.')



# ---------------------------- UI SETUP ------------------------------- #
app = Tk() 
app.title('Password Manager') 
app.config(padx = 50, pady = 20, bg = YELLOW)


canvas = Canvas(width=200, height=200, bg = YELLOW, highlightthickness= 0)
password_img = ImageTk.PhotoImage(Image.open("password generator/password.png"))
canvas.create_image(100, 100, image=password_img)
canvas.grid(column = 1, row = 0)

# Labels 
website = Label(text = 'Website:', bg = YELLOW)
website.grid(column=0, row = 1)
email = Label(text = 'Email:', bg = YELLOW)
email.grid(column=0, row = 2)
password = Label(text = 'Password:', bg = YELLOW)
password.grid(column=0, row = 3)

# Entries 
website_entry = Entry(width = 36, highlightbackground= YELLOW)
website_entry.grid(column =1, row=1, sticky="EW")
website_entry.focus()
email_entry = Entry(width = 36, highlightbackground= YELLOW) 
email_entry.grid(column = 1, row= 2, columnspan=2, sticky="EW")
email_entry.insert(0, '@gmail.com')
#password_entry = Entry(width = 18, highlightbackground= YELLOW)
password_entry = Entry(app, show = '*', width = 18, highlightbackground= YELLOW)
password_entry.grid(column = 1, row = 3, stick = 'EW')

# Buttons 
generate_pass = Button(text = 'Generate Password', bg = YELLOW, highlightbackground= YELLOW, command = generate_password, width = 13)
generate_pass.grid(column = 2, row = 3, sticky="EW")
store_creds = Button(text = 'Store', highlightbackground= YELLOW, width = 35, command = save)
store_creds.grid(column = 1, row = 4, columnspan=2, sticky="EW")
search_creds = Button(text = 'Search', bg = YELLOW, highlightbackground= YELLOW, width = 13, command = find_password)
search_creds.grid(column = 2, row = 1, sticky = 'EW') 

app.mainloop()
