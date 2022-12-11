# Pomodoro
from tkinter import *
import time
import math
# --------------------- CONSTANTS ---------------------------#
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
# colors for easier access
# https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
reps = 0
timer = None
# --------------------- Timer Reset ---------------------------#
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")

# --------------------- TIMER MECHANISM ---------------------------#
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0 :
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
 
# --------------------- COUNTDOWN MECHANISM ---------------------------#
def count_down(count):
    # timer format 00:00
    count_min = math.floor(count / 60 )
    count_sec = count % 60
 
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0 :
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
            check_marks.config(text=mark)

    
# --------------------- UI SETUP ---------------------------#
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="C:/Users/mahan/Desktop/100DaysOfCodePython-master/day28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130 , text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Title Label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

# Button Start
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0 , row=3)

# Check Label
check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "normal"))
check_marks.grid(column=1, row=4)

# Button Reset
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=3 , row=3)

window.mainloop()