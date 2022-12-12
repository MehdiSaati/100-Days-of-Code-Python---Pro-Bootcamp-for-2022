from tkinter import *
from tkinter import messagebox
from random import random, randint, shuffle, choice
import pyperclip
# ------------------- PASSWORD GENERATOR ---------------------#
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #new_list = [new_item for item in list]
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
        
    # Shuffle a list (reorganize the order of the list items)   
    shuffle(password_list)

    # Convert list to string
    password = "".join(password_list) 
    password_entery.insert(0, password)
    pyperclip.copy(password)

# ------------------- SAVE PASSWORD ---------------------#
import os
os.chdir("/Users/mahan/Desktop/100DaysOfCodePython-master/day29")
def save():
    website = website_entery.get()
    email = email_entery.get()
    password = password_entery.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered: \n Email: {email}\n Password: {password}\n Is it ok to save?")
        if is_ok == True:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                website_entery.delete(0, END)
                password_entery.delete(0, END)
 

# ------------------- UI SETUP ---------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200 , height=200)
logo_img = PhotoImage(file="C:/Users/mahan/Desktop/100DaysOfCodePython-master/day29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Label
website_label = Label(text="Website : " , font=("Arial", 8, "bold"))
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username : " , font=("Arial", 8, "bold"))
email_label.grid(column=0, row=2)
password_label = Label(text="Password : " , font=("Arial", 8, "bold"))
password_label.grid(column=0, row=3)

# Entries
website_entery = Entry(width=35)
website_entery.grid(column=1, row=1 , columnspan=2)
website_entery.focus()
email_entery = Entry(width=35)
email_entery.grid(column=1, row=2 , columnspan=2)
email_entery.insert(0,"example@gmail.com")
password_entery = Entry(width=17)
password_entery.grid(column=1, row=3)

# Buttons
password_generator_button = Button(text="Generate Password", command=generate_password)
password_generator_button.grid(column=2, row=3)
add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()