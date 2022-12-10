# Miles to Km Converter
from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#Lable miles
miles_lable = Label(text="Miles", font=("Arial", 10, "bold"))
miles_lable.grid(column=3, row=0)

#Lable km
kilometer_lable = Label(text="Km", font=("Arial", 10, "bold"))
kilometer_lable.grid(column=3, row=1)

#Lable is equal
is_equal_lable = Label(text="is equal to ", font=("Arial", 10, "bold"))
is_equal_lable.grid(column=1, row=1)

#Lable is covert
kilometer_result_lable = Label(text="0 ", font=("Arial", 10, "bold"))
kilometer_result_lable.grid(column=2, row=1)

# Button
def miles_to_km():
    miles = float(miles_input.get()) 
    km = round(miles * 1.609)
    kilometer_result_lable.config(text=f"{km}")

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=2, row=2)

# Input
miles_input = Entry(width=7)
miles_input.grid(column=2, row=0)

window.mainloop()