from tkinter import *


# Button Component
def button_clicked():
    print("I got clicked")
    user_input = input.get()
    my_label.config(text=user_input)


window = Tk()
window.title("GUI Program")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

# Label Component
my_label = Label(text="I Am a Label", font=("Arial", 20, "bold"))
my_label.config(text="New Text")
my_label.config(padx=50, pady=50)
my_label.grid(column=0, row=0)

# Button Component
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button = Button(text="I am a button", command=button_clicked)
button.grid(column=2, row=0)

# Entry component (input)
input = Entry(width=30)
input.focus()
input.grid(column=3, row=2)

window.mainloop()
