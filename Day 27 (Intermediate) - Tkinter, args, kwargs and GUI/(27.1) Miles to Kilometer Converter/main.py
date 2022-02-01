from tkinter import *


def convert():
    user_input = float(input.get())
    calculation = round((user_input * 1.60934), 3)
    lb_conversion.config(text=calculation)

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=200, height=0)
window.config(padx=20, pady=20)

# Creating Labels
lb_isequalto = Label(text="Is Equal To")
lb_miles = Label(text="Miles")
lb_km = Label(text="Km")
lb_conversion = Label(text="0")

# Placing them on a grid
lb_isequalto.grid(column=0, row=1)
lb_miles.grid(column=2, row=0)
lb_km.grid(column=2, row=1)
lb_conversion.grid(column=1, row=1)

# Creating Entry Component
input = Entry(width=20)
input.focus()
input.grid(column=1, row=0)

# Creating a button
btn_calculate = Button(text="Calculate", command=convert)
btn_calculate.grid(column=1, row=2)

window.mainloop()
