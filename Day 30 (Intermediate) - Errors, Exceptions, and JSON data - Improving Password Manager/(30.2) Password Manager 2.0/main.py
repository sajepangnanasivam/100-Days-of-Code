from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import choice, randint, shuffle
import pyperclip
import json

# Paddings
WIN_PADDING = 75
LB_PADY = 8
LB_PADX = 10

# STYLING
RED = "#cccccc"
FONT_NAME = "Calibri"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    input_website_password.delete(0, END)
    input_website_password.insert(0, password)


# ---------------------------- SEARCH DATA ------------------------------- #
def find_password():
    website = input_website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found.")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username:\t{username}\nPassword:\t{password}")
        else:
            messagebox.showerror(title=f"Error", message=f"No Entry for {website} Exist.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    """ Function to save data to data.csv with open method
    """
    data_website = str(input_website.get())
    data_username = str(input_email_username.get())
    data_password = str(input_website_password.get())
    new_data = {
        data_website: {
            "username": data_username,
            "password": data_password
        }
    }

    if len(data_username) == 0 or len(data_password) == 0 or len(data_website) == 0:
        messagebox.showwarning(title="❌ Input Warning", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Delete the input after writing to file.
            input_website.delete(0, END)
            input_website_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# TODO: Create window
window = Tk()
window.title("🔑 Password Manager")
window.config(padx=WIN_PADDING, pady=WIN_PADDING, bg=RED)

# TODO: Create Canvas
canvas = Canvas(width=200, height=200, bg=RED, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0, columnspan=2)

# TODO: Creating Labels
lb_website = Label(text="Website:", bg=RED, pady=LB_PADY, padx=LB_PADX, font=(FONT_NAME, 11, "bold"))
lb_email_username = Label(text="Email/Username:", bg=RED, pady=LB_PADY, padx=LB_PADX, font=(FONT_NAME, 11, "bold"))
lb_password = Label(text="Password:", bg=RED, pady=LB_PADY, padx=LB_PADX, font=(FONT_NAME, 11, "bold"))

lb_website.grid(column=0, row=1, sticky=W)
lb_email_username.grid(column=0, row=2, sticky=W)
lb_password.grid(column=0, row=3, sticky=W)

# TODO: Create Entries
input_website = Entry(width=24)
input_email_username = Entry(width=50)
input_website_password = Entry(width=24)
input_website.focus()
input_email_username.insert(0, "Brian_Vance@gmail.com")

input_website.grid(column=1, row=1, columnspan=2, sticky="W")
input_email_username.grid(column=1, row=2, columnspan=2, sticky="EW")
input_website_password.grid(column=1, row=3, sticky="EW")

# TODO: Create buttons
btn_gen_pass = Button(text="Generate Password", width=20, relief=FLAT, highlightthickness=0, command=generate_password)
btn_add = Button(text="Add", width=36, height=2, relief=FLAT, highlightthickness=0, command=save_data)
btn_search = Button(text="Search", width=20, relief=FLAT, highlightthickness=0, command=find_password)

btn_gen_pass.grid(column=2, row=3, sticky=E)
btn_add.grid(column=1, row=4, columnspan=2, sticky=EW)
btn_search.grid(column=2, row=1, sticky=E)

window.mainloop()
