#TODO: asking the questions
#TODO: Checking if the answer was correct
#TODO: Checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        length_q_list = len(self.question_list)
        # Returns false if the statement is false
        return self.question_number < length_q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        # To show correct question number
        self.question_number += 1
        user_answer = input(f"🧠 Q.{self.question_number}:\t {current_question.text} (True/False)?\t ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("✔ Correct answer!")

        else:
            print("❌ That's wrong ..")
        print(f"👓 The correct answer:\t {correct_answer}")
        print(f"🥅 Your current score is:\t {self.score}/{self.question_number}")
        print("------------------------------------------\n")

        # Method 1: When the user completes the Quiz.
        # Method 2 in main.py
        #if self.question_number == len(self.question_list):
        #    print("✔ You've Completed the Quiz!")
        #    print(f"🥅 Your final score was {self.score}/{self.question_number}")




