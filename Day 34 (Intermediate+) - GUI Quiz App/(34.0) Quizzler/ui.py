from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Creating label and placing on grid
        self.lb_score = Label(text="Score: 0", foreground="white", bg=THEME_COLOR)
        self.lb_score.grid(row=0, column=1)

        # Creating a canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 126,
            width=270,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 16, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Creating buttons and placing on grid
        img_true = PhotoImage(file="images/true.png")
        img_false = PhotoImage(file="images/false.png")
        self.btn_true = Button(image=img_true, highlightthickness=0, command=self.true_pressed)
        self.btn_false = Button(image=img_false, highlightthickness=0, command=self.false_pressed)
        self.btn_true.grid(row=2, column=0)
        self.btn_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.lb_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz!")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

