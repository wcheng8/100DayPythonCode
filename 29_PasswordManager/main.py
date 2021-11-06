from tkinter import *
from Password import Password
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
# Save password to file
def add_pass():
    new_pass = Password()
    new_pass.password = password_entry.get()
    new_pass.username = username_entry.get()
    new_pass.site = website_entry.get()
    password = new_pass.print_pas()
    pass_verify = pass_len_verify(new_pass)
    if pass_verify:
        user_verify = messagebox.askokcancel(title='Please verify', message=f'Is the username and password of: \nUsername: {new_pass.username}\nPassword:{new_pass.password}\nWhat you wanted?')
        if user_verify:
            with open('password_file.txt', 'a') as file:
                file.write(password + '\n')
            messagebox.showinfo(message='Password has been successfully added!')
            reset()
    else:
        messagebox.showinfo(message='Password must be at least 8 characters long. :(')
        reset()

def pass_len_verify(new_pass):
    if len(new_pass.password) >= 8:
        return True
    return False

def reset():
    password_entry.delete(0, 'end')
    username_entry.delete(0,'end')
    username_entry.insert(0,'user@admin.com')
    website_entry.delete(0,'end')
    website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=lock_img)
canvas.grid(column=1, row=0)

# Buttons/Text
website_txt = Label(text='Website')
username_txt = Label(text='Email/Username')
password_txt = Label(text='Password')
website_txt.grid(column=0, row=1)
username_txt.grid(column=0, row=2)
password_txt.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.insert(0,'user@admin.com')
password_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=2)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

gen_pass_btn = Button(text='Generate Password', width = 14,command=gen_pass)
add_btn = Button(text='Add', width=36, command=add_pass)
gen_pass_btn.grid(column=2, row=3)
add_btn.grid(column=1, row=4, columnspan=2)




window.mainloop()
