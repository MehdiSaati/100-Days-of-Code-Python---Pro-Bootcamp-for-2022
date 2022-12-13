from tkinter import *
from tkinter import messagebox
from random import random, randint, shuffle, choice
import pyperclip
import json 

# ------------------- Find Password ---------------------#
def find_password():
    website = website_entry.get()
 
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:              
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email : {email}\n Password : {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ------------------- PASSWORD GENERATOR ---------------------#
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
 
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers 

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ------------------- SAVE PASSWORD ---------------------#
import os
os.chdir("/Users/mahan/Desktop/100DaysOfCodePython-master/day30/Password-Manager-v2")
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 :
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:

        is_ok = messagebox.askokcancel(title= f"{website}", message=f"These are the details entered: \n Email: {email}\n Password: {password}\n Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

            finally:
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)

# ------------------- UI SETUP ---------------------#
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(125, 100, image=logo_image)
canvas.grid(column=1, row=0)

#Label
website_label = Label(text="Website : ")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username : ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=34)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=53)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "Email@example.com" )

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

# Buttons
button_search = Button(text="Search", width=15, command=find_password )
button_search.grid(column=2, row=1)

button_generate_password = Button(text="Generate Password", command=generate_password )
button_generate_password.grid(column=2, row=3)

button_add = Button(text="Add", width=45, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()