import tkinter as ttk

window = ttk.Tk()
window.title('Food Converter')
window.config(padx=20, pady=20)


def cup_to_g_flour():
    cup = float(entry_cup.get())
    grams = cup * 136
    entry_g.config(text=f'{grams}')


def cup_to_g_sugar():
    cup = float(entry_cup.get())
    grams = cup * 201
    entry_g.config(text=f'{grams}')


entry_cup = ttk.Entry(text='Cups', width=10)
entry_cup.grid(column=1, row=2)

label_cup = ttk.Label(text='Cups')
label_cup.grid(column=2, row=2)

entry_g = ttk.Label(width=10)
entry_g.grid(column=1, row=3)

label_g = ttk.Label(text='Grams')
label_g.grid(column=2, row=3)

convert_button_f = ttk.Button(text='Convert Flour', command=cup_to_g_flour)
convert_button_f.grid(column=1, row=5)

convert_button_s = ttk.Button(text='Convert Sugar', command=cup_to_g_sugar)
convert_button_s.grid(column=2, row=5)

window.mainloop()
