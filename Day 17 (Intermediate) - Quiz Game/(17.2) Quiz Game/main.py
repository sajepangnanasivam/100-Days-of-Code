from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []

# Creating a Question bank from question_data.py.
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("✔ You've Completed the Quiz!")
print(f"🥅 Your final score was {quiz.score}/{quiz.question_number}")