from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


# ---------------- SHOW NEXT CARD ---------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # Background
    canvas.itemconfig(canvas_image, image=img_front_card)
    # Text
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


# ---------------- FLIP CARD ---------------- #
def flip_card():
    # Background
    canvas.itemconfig(canvas_image, image=img_back_card)
    # Text
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------- USER INTERFACE ---------------- #
# TODO: Create window
window = Tk()
window.title("🃏 Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# TODO: Init Images from folder
img_front_card = PhotoImage(file="images/card_front.png")
img_back_card = PhotoImage(file="images/card_back.png")
img_right = PhotoImage(file="images/right.png")
img_wrong = PhotoImage(file="images/wrong.png")

# TODO: Create the canvas
canvas = Canvas(width=800, height=560, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=img_front_card)
canvas.grid(column=0, row=0, columnspan=2)
# Creating the text
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 30, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 50, "bold"))

# TODO: Create buttons from images
btn_right = Button(image=img_right, bg=BACKGROUND_COLOR, relief=FLAT, highlightthickness=0, command=is_known)
btn_wrong = Button(image=img_wrong, bg=BACKGROUND_COLOR, relief=FLAT, highlightthickness=0, command=next_card)
btn_right.grid(column=1, row=1)
btn_wrong.grid(column=0, row=1)

next_card()

window.mainloop()
