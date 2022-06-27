from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk, Image
import random 
import pyperclip 

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
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password) 
    # password = ""
    # for char in password_list:
    #     password += char

    # print(f"Your password is: {password}")
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(): 

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0: 
        messagebox.showinfo(title = 'Error', message = "Please make sure you don't have any empty fields.")
    
    else: 
        is_ok = messagebox.askokcancel(title= website_entry.get(), message = f'The credentials you have entered: \nEmail: {email_entry.get()}\nPassword: {password_entry.get()}\nPress OK to save.')

        if is_ok: 
            with open('password generator/data.txt', 'a') as f: 
                f.write(f'{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n')

    website_entry.delete(0, END)
    password_entry.delete(0, END)

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
website_entry.grid(column =1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry(width = 36, highlightbackground= YELLOW) 
email_entry.grid(column = 1, row= 2, columnspan=2, sticky="EW")
email_entry.insert(0, '@gmail.com')
#password_entry = Entry(width = 18, highlightbackground= YELLOW)
password_entry = Entry(app, show = '*', width = 18, highlightbackground= YELLOW)
password_entry.grid(column = 1, row = 3, stick = 'EW')

# Buttons 
generate_pass = Button(text = 'Generate Password', bg = YELLOW, highlightbackground= YELLOW, command = generate_password)
generate_pass.grid(column = 2, row = 3, sticky="EW")
store_creds = Button(text = 'Store', highlightbackground= YELLOW, width = 35, command = save)
store_creds.grid(column = 1, row = 4, columnspan=2, sticky="EW")

app.mainloop()
