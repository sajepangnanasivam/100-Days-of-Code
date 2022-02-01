from tkinter import *
import math
import time

# ---------------------------- CONSTANTS ------------------------------- #
RED = "#E23E57"
RED2 = "#F38181"
YELLOW = "#FFD460"
PASTELYELLOW = "#EAFFD0"
BLUE = "#3490DE"
GREEN = "#9BDEAC"
FONT_NAME = "Courier"
reps = 0
timer = NONE

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BTN_W, BTN_H = 8, 2


# ---------------------- TIMER RESET ---------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    lb_title.config(text="Timer")
    lb_checkmark.config(text="")
    global reps
    reps = 0


# ---------------------- TIMER MECHANISM ------------------------ #
def start_timer():
    global reps
    reps += 1

    t_work = WORK_MIN * 60
    t_shortBreak = SHORT_BREAK_MIN * 60
    t_longBreak = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        lb_title.config(text="Break", bg=RED2, fg=BLUE, font=(FONT_NAME, 35, "bold"))
        count_down(t_longBreak)
    elif reps % 2 == 0:
        lb_title.config(text="Break", bg=RED2, fg=RED, font=(FONT_NAME, 35, "bold"))
        count_down(t_shortBreak)
    else:
        lb_title.config(text="Work", bg=RED2, fg=GREEN, font=(FONT_NAME, 35, "bold"))
        count_down(t_work)


# ---------------------- COUNTDOWN MECHANISM -------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        lb_checkmark.config(text=marks)


# ---------------------- UI SETUP ------------------------------- #
# TODO: Setup the Tkinter window
window = Tk()
window.title("🍅 Pomodoro")
window.config(height=500, width=600, padx=100, pady=100, bg=RED2)

# TODO: Create CANVAS
canvas = Canvas(width=200, height=224, bg=RED2, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# TODO: Create BUTTONS
btn_start = Button(text="Start", width=BTN_W, height=BTN_H, relief=FLAT, highlightthickness=0, command=start_timer)
btn_reset = Button(text="Reset", width=BTN_W, height=BTN_H, relief=FLAT, highlightthickness=0, command=reset_timer)

btn_start.grid(column=0, row=2)
btn_reset.grid(column=2, row=2)

# TODO: Create LABEL
lb_title = Label(text="Timer", bg=RED2, fg=YELLOW, font=(FONT_NAME, 35, "bold"))
lb_title.grid(column=1, row=0)

# TODO: Create CHECKMARKS
lb_checkmark = Label(text=" ", bg=RED2, fg=GREEN, font=(FONT_NAME, 14, "bold"))
lb_checkmark.grid(column=1, row=3)

window.mainloop()
