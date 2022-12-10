from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=250, height= 150)
window.config(padx=10, pady=10)

#Lable
my_lable = Label(text="I Am a Label", font=("Arial", 20, "bold"))
my_lable.grid(column=0, row=0)

my_lable["text"] = "New text"
my_lable.config(text="New text")

# Button
def button_clicked():
    # my_lable.config(text="Button Got Clicked")
    new_text = input.get()
    my_lable.config(text=new_text)

my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Input
input = Entry(width=9)
input.grid(column=3, row=3)



window.mainloop()