from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ('Arial',20,'italic')

class QuizInterface:
    def __init__(self,quiz: QuizBrain):
        self.quiz_brain = quiz
        self.window = Tk()
        self.window.title("Quizzet")
        self.window.config(padx = 20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300,height=250,bg='white')
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text=f'Question Here',
            font=FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1,column=0,columnspan=2,pady = 50)

        self.score = 0
        self.score_txt = Label(text=f'Score: {self.score}', fg='white', bg=THEME_COLOR)
        self.score_txt.grid(row=0, column=1)
        true_img = PhotoImage(file='./images/true.png')
        false_img = PhotoImage(file='./images/false.png')
        self.true_btn = Button(image=true_img,highlightthickness = 0,command=self.true)
        self.false_btn = Button(image=false_img,highlightthickness=0,command=self.false)
        self.true_btn.grid(row=2,column=0)
        self.false_btn.grid(row=2,column=1)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        question = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question, text=f'{question}')

    def true(self):
        if self.quiz_brain.check_answer('True') and self.quiz_brain.still_has_questions():
            self.score += 10
            self.score_txt.config(text=f'Score: {self.score}')

        self.check_still_has_question_print_score()

    def false(self):
        self.check_still_has_question_print_score()

    def check_still_has_question_print_score(self):
        if self.quiz_brain.still_has_questions():
            self.next_question()
        else:
            no_of_questions = self.quiz_brain.question_number
            question_correct = self.quiz_brain.score
            self.canvas.itemconfig(self.question,text=f'You obtained a final score of {self.score}.\nYou got {question_correct}/{no_of_questions} questions correct!')
