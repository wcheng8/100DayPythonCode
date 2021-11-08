from tkinter import *
import pandas as pd
from random import choice
from flashcard import flashcard
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ('Ariel',40,'italic')
FONT_WORD = ('Ariel',60,'bold')
all_flashcards = []

# Get Flashcard data from csv and populate data
data = pd.read_csv('./data/french_words.csv')
for word, answer in data.iterrows():
    new_flashcard = flashcard(word, answer)
    all_flashcards.append(new_flashcard)

# Determine Correct and Wrong
def wrong():
    pass

def correct():
    pass

# UI Setup
window = Tk()
window.title("Language Flash card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=card_img)
canvas.create_text(400,150,text='French', font=FONT_LANGUAGE)
flash_front = canvas.create_text(400,263,text='Word', font=FONT_WORD)
canvas.grid(row=0, column=0,columnspan=2)

wrong_img = PhotoImage(file='./images/wrong.png')
right_img = PhotoImage(file='./images/right.png')
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=wrong)
correct_btn = Button(image=right_img, highlightthickness=0, command=correct)
wrong_btn.grid(row=1, column=1)
correct_btn.grid(row=1, column=0)

window.mainloop()



