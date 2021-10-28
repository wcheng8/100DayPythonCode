from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for pair in question_data:
    new_question = Question(pair["text"], pair["answer"])
    question_bank.append(new_question)
play_again = True
while play_again:
    quiz_master = QuizBrain(question_bank)
    # TODO 1. asking the questions
    # TODO 2. checking if the answer was correct
    while(quiz_master.still_has_questions()):
        answer = quiz_master.next_question()
        quiz_master.check_answer(answer)

    # TODO 3. checking if we're at the end of the quiz
    repeat = input(f"We are at the end of the quiz. Your final score is {quiz_master.score}/12. Would you like to play again? (y/n) ")
    play_again = True if repeat == 'y' else False