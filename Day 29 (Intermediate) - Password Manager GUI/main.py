from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import choice, randint, shuffle
import pyperclip

# Paddings
WIN_PADDING = 75
LB_PADY = 8
LB_PADX = 10
INPUT_WIDTH = 50

# STYLING
RED = "#cccccc"
FONT_NAME = "Calibri"
data_file = pd.read_csv("data.csv")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data_pandas():
    """ Function to save data to data.csv with pandas
    """
    global data_file
    temp_data = []
    data_website = str(input_website.get())
    data_username = str(input_email_username.get())
    data_password = str(input_website_password.get())
    data_dict = {"Website": data_website,
                 "Username": data_username,
                 "Password": data_password
                 }
    if len(data_username) == 0 or len(data_password) == 0 or len(data_website) == 0:
        messagebox.showwarning(title="❌ Input Warning", message="Please don't leave any fields empty!")
    else:
        msg_ok = messagebox.askokcancel(title=f"🌐 Website: {data_website}",
                                        message=f"These are the details entered:"
                                                f"\n📧 Email:\t\t {data_username}"
                                                f"\n🔑 Password:\t {data_password}")
        if msg_ok:
            temp_data.append(data_dict)
            temp_data_df = pd.DataFrame(temp_data)
            temp_data_df.to_csv("data.csv", mode="a", index=False, header=False)
            input_website.delete(0, END)
            input_website_password.delete(0, END)


def save_data_open():
    """ Function to save data to data.csv with open method
    """
    data_website = str(input_website.get())
    data_username = str(input_email_username.get())
    data_password = str(input_website_password.get())
    if len(data_username) == 0 or len(data_password) == 0 or len(data_website) == 0:
        messagebox.showwarning(title="❌ Input Warning", message="Please don't leave any fields empty!")
    else:
        msg_ok = messagebox.askokcancel(title=f"🌐 Website: {data_website}",
                                        message=f"These are the details entered:"
                                                f"\n📧 Email:\t\t {data_username}"
                                                f"\n🔑 Password:\t {data_password}")
        if msg_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{data_website} | {data_username} | {data_password}\n")
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
input_website = Entry(width=INPUT_WIDTH)
input_email_username = Entry(width=INPUT_WIDTH)
input_website_password = Entry()
input_website.focus()
input_email_username.insert(0, "Brian_Vance@gmail.com")

input_website.grid(column=1, row=1, columnspan=2, sticky="EW")
input_email_username.grid(column=1, row=2, columnspan=2, sticky="EW")
input_website_password.grid(column=1, row=3, sticky="EW")

# TODO: Create buttons
btn_gen_pass = Button(text="Generate Password", width=20, relief=FLAT, highlightthickness=0, command=generate_password)
btn_add = Button(text="Add", width=36, height=2, relief=FLAT, highlightthickness=0, command=save_data_open)

btn_gen_pass.grid(column=2, row=3, sticky=E)
btn_add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
