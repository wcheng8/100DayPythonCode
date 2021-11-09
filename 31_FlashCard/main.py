from tkinter import *
import pandas as pd
from random import choice
from flashcard import flashcard
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ('Ariel',40,'italic')
FONT_WORD = ('Ariel',60,'bold')
all_flashcards = []
current_card = {}
# Get Flashcard data from csv and populate data
data = pd.read_csv('./data/french_words.csv')
for index, pair in data.iterrows():
    new_flashcard = flashcard(index, pair['French'], pair['English'])
    all_flashcards.append(new_flashcard)

def quit_save():
    # Save words to learn to a csv
    new_d = {'French':[],'English':[]}
    for flashcard in all_flashcards:
        new_d['French'].append(flashcard.word)
        new_d['English'].append(flashcard.answer)
    df = pd.DataFrame(new_d)
    df.to_csv('./data/new_words_to_learn.csv')
    window.destroy()

def flip_card():
    canvas.itemconfig(card_front, image=card_back)
    canvas.itemconfig(language, text='English', font=FONT_LANGUAGE, fill='white')
    canvas.itemconfig(flash_front, text=f'{current_card.answer}')

# Determine Correct and Wrong
def wrong():
    canvas.itemconfig(flash_front, text=f'{choice(all_flashcards).word}')
    next_card()

def correct():
    canvas.itemconfig(flash_front, text=f'{choice(all_flashcards).word}')
    all_flashcards.remove(current_card)
    # print(len(all_flashcards))
    next_card()
# UI Setup
window = Tk()
window.title("Language Flash card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_img = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
card_front = canvas.create_image(400, 263, image=card_img)
language = canvas.create_text(400,150,text='French', font=FONT_LANGUAGE)
flash_front = canvas.create_text(400,263,text='Word', font=FONT_WORD)
canvas.grid(row=0, column=0,columnspan=2)

wrong_img = PhotoImage(file='./images/wrong.png')
right_img = PhotoImage(file='./images/right.png')
quit_img = PhotoImage(file='./images/quit.png')
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=wrong)
correct_btn = Button(image=right_img, highlightthickness=0, command=correct)
quit_btn = Button(image=quit_img, highlightthickness=0, command=quit_save )
wrong_btn.grid(row=1, column=1)
correct_btn.grid(row=1, column=0)
quit_btn.grid(row=2, column = 0, columnspan=2)
flip_timer = window.after(3000, func=flip_card)

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(all_flashcards)
    canvas.itemconfig(language, text = 'French', fill='black')
    canvas.itemconfig(flash_front, text=f'{current_card.word}', fill='black')
    canvas.itemconfig(card_front, image=card_img)
    flip_timer = window.after(3000, func=flip_card)

next_card()

window.mainloop()



