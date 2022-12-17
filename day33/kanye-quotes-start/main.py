# Kanye Quotes
import requests
from tkinter import *
import os
os.chdir("/Users/mahan/Desktop/100DaysOfCodePython-master/day33/kanye-quotes-start")

# --------------------- GET Quote ---------------------------#
def get_quote():
    response = requests.get(url="https://api.themotivate365.com/stoic-quote")
    # response = requests.get(url = "https://api.kanye.rest")
    response.raise_for_status()

    data = response.json()
    quote = data["quote"]
    author = data["author"]
    canvas.itemconfig(quote_text, text= quote)
    canvas.itemconfig(author_text, text= author)

# --------------------- SETUP UI ---------------------------#
window = Tk()
window.title("Kanye Quotes")
window.config(padx=50, pady= 50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
canvas.grid(row=0, column=0)

quote_text = canvas.create_text(150, 120, text="", width=250, fill="white", font=("Ariel", 16, "normal"))
author_text = canvas.create_text(150, 320, text="", width=250, font=("Ariel", 18, "bold"))
kanye_img = PhotoImage(file="kanye.png")
kaney_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kaney_button.grid(row=1, column=0)

get_quote()
window.mainloop()