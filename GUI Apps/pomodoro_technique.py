# pomodoro technique 

# outline: 
    # decide the task that you need to do 
    # set a timer to 25 minutes 
    # work on the task for the set duration 
    # take a short 5 minute break 
    # repeat 4 times
    # take 15-30 minutes break 


from tkinter import * 
from PIL import ImageTk, Image
import math 

# ---------------------------- CONSTANTS ------------------------------- #
# https://colorhunt.cohttps://colorhunt.co
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer(): 
    app.after_cancel(timer)
    
    # things to reset : timer_text, title_label, check_marks 
    canvas.itemconfig(timer_text, text = '00:00')
    title_label.config(text = 'Timer')
    check_marks.config(text = '')
    global reps 
    reps = 0 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(): 

    global reps 
    reps +=1 

    work_seconds = WORK_MIN * 60 
    short_break_seconds = SHORT_BREAK_MIN * 60 
    long_break_seconds = LONG_BREAK_MIN * 60 

    # 8th rep 
    if reps % 8 == 0: 
        countdown(long_break_seconds)
        title_label.config(text= 'Break', fg = RED)
    # 2nd, 4th, 6th rep 
    elif reps % 2 == 0: 
        countdown(short_break_seconds)
        title_label.config(text= 'Break', fg = PINK)
    else: 
    # 1st, 3rd, 5th, 7th rep
        countdown(work_seconds)
        title_label.config(text= 'Work', fg = GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count): 
    
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10: 
        count_seconds = f'0{count_seconds}'

    canvas.itemconfig(timer_text, text = f'{count_minute}:{count_seconds}')
    if count > 0: 
        global timer 
        timer = app.after(1000, countdown, count -1)
    else: 
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✅'
        check_marks.config(text = marks)


# ---------------------------- UI SETUP ------------------------------- #
app = Tk() 
app.title('Pomodoro') 
app.config(padx = 100, pady = 50, bg = YELLOW)



title_label = Label(text='Timer', font = (FONT_NAME, 50, 'bold'), fg = GREEN, bg = YELLOW)
title_label.grid(column = 1, row = 0)

canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness= 0)
tomato_img = ImageTk.PhotoImage(Image.open("pomodoro/tomato.png"))
#tomato_img = PhotoImage(file = 'pomodoro/tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text = '00:00', fill = 'white', font = (FONT_NAME, 35, 'bold'))
canvas.grid(column = 1, row = 1)


start_button = Button(text = 'Start', command = start_timer, highlightthickness= 0)
start_button.grid(column =0, row =2)
reset_button = Button(text = 'Reset', command = reset_timer, highlightthickness= 0)
reset_button.grid(column =2, row =2)

check_marks = Label(fg = GREEN, bg = YELLOW)
check_marks.grid(column = 1, row=3)




# event driven --> while loops won't work with mainloop 
app.mainloop()