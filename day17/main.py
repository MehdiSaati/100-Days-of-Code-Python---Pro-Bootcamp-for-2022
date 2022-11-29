from question_model import Question
from data import question_data
from quize_brain import QuizBrain
import random

question_bank =[]

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].text)
quiz = QuizBrain(question_bank)
flag = quiz.has_still_question()
while flag:
    quiz.next_question()

print(f"You've compelted the quiz")
print(f"Your final score was: {quiz.score} / {quiz.question_number}")
