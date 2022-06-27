##################################################
######## Miles to kilometer converter v2 #########
##################################################

from tkinter import * 

app = Tk()
app.title('Miles to Kilometers Converter') 
app.minsize(width = 150, height = 150)
app.config(padx = 20, pady = 20)
FONT = ('Courier', 18, 'bold')

def miles_to_km(): 
    miles_or_km_input_label.config(text = 'Mile(s)')
    miles_or_km_output_label.config(text = 'Kilometer(s)')
    miles = float(input.get())
    km = round(miles * 1.609,3)
    result.config(text = f'{km}')

def km_to_miles(): 
    miles_or_km_input_label.config(text = 'Kilometer(s)')
    miles_or_km_output_label.config(text = 'Mile(s)')
    km = float(input.get())
    miles = round(km/1.609 ,3)
    result.config(text = f'{miles}')

def reset():
    input.delete(first=0, last=7)
    result.config(text="0")

#Radiobutton
def radio_used():
    if radio_state.get() == 1: 
        miles_to_km()
    elif radio_state.get() == 2: 
        km_to_miles() 
    
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Mile(s) to Kilometer(s)", value=1, variable=radio_state, command=radio_used, font = FONT)
radiobutton2 = Radiobutton(text="Kilomter(s) to Mile(s)", value=2, variable=radio_state, command=radio_used, font = FONT)
radiobutton1.grid(column = 1, row = 2)
radiobutton2.grid(column = 1, row = 3)


input = Entry(width = 7, font = FONT)
input.grid(column = 1, row = 0)

miles_or_km_input_label = Label(text = 'Mile(s)', font = FONT) 
miles_or_km_input_label.grid(column = 2, row = 0)

is_equal_label = Label(text = 'is roughly equal to', font = FONT) 
is_equal_label.grid(column = 0, row = 1)

result = Label(text = '0', font = FONT) 
result.grid(column = 1, row = 1)

miles_or_km_output_label = Label(text= 'Kilometer(s)', font = FONT)
miles_or_km_output_label.grid(column = 2, row = 1)

button = Button(text = 'Reset', command = reset, font = FONT)
button.grid(column = 3, row = 3)
