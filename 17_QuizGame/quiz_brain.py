class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        return answer

    def still_has_questions(self):
        number_of_questions = len(self.question_list)
        return not number_of_questions == self.question_number

    def check_answer(self, answer):
        current_question_pair = self.question_list[self.question_number-1]
        if answer == current_question_pair.answer:
            print("You are correct!")
            self.score += 1
            print(f"Score: {self.score}/{self.question_number}")
        else:
            print("Try again next time :(")
            print(f"Score: {self.score}/{self.question_number}")



