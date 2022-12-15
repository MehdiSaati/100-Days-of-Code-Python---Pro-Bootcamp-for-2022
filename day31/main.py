from tkinter import *
import pandas
import random
import os
os.chdir("/Users/mahan/Desktop/100DaysOfCodePython-master/day31")

BACKGROUND_COLOR ="#B1DDC6"
current_card = {}
to_learn = {}
# ------------------------------- Open csv file -----------------------------------#
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    orginal_data = pandas.read_csv("./data/french_words.csv")
    to_learn = orginal_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    
# ------------------------------- Next Card -----------------------------------#
def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text= "French", fill="black")   
    canvas.itemconfig(card_word, text= current_card["French"], fill="black")  
    canvas.itemconfig(card_background, image=card_front_image) 
    flip_timer = window.after(3000, func=flip_card)

# ------------------------------- Flip Card -----------------------------------#
def flip_card():
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(card_title, text= "English", fill="white")   
    canvas.itemconfig(card_word, text= current_card["English"], fill="white")  

# ------------------------------- Is Known -----------------------------------#

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=FALSE)
    next_card()

# ------------------------------- UI Setup -----------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "bold"))

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()