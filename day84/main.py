from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont
import os

os.chdir("/Users/mahan/Desktop/100DaysOfCodePython-master/day84")

FONT_NAME = "Courier"
Orange = "#f24c0a"
YELLOW = "#fdffe8"

root = Tk()
root.title('IMAGE WATERMARK')
root.config(padx=25, pady=25)
img_file = ''

def select_file():
    global img_file
    img_file = askopenfilename()

def watermark(img_input, img_output, text_watermark, xy_pos):
    image = Image.open(img_input)

    edit_image = ImageDraw.Draw(image)

    sky_blue = (242, 76, 10)
    font_watermark = ImageFont.truetype("arial.ttf", 200)
    edit_image.text(xy_pos, text_watermark, font= font_watermark, fill= sky_blue)
    image.show()
    image.save(img_output)

def watermark_img():
    if img_file == '':
        messagebox.showerror("No image found", "Please select an image first")
    else:
        img_output = f'watermark.jpg'
        text_watermark = text_entery.get()
        watermark(img_file, img_output, text_watermark= text_watermark, xy_pos=(100,100))
        messagebox.showinfo("Complete", "Successfully watermarked!")

title_label = Label(text="IMG Watermark", font=(FONT_NAME, 50, "bold"), fg=Orange, bg=YELLOW)
title_label.grid(column=0, row=1, rowspan=4)

b1 = Button(root, text="1. Select Image", font=20, width=15,
 command=select_file)

text_label = Label(text="2. Watermark Text", font=20)

text_entery = Entry(width=26)

b2 = Button(root, text="3. Watermark IMG", font=20, width=15,
command=watermark_img)


b1.grid(column=1, row=1, columnspan=2, padx=25, pady=25)
text_label.grid(column=1, row=2, columnspan=2, padx=25, pady=25)
text_entery.grid(column=1, row=3, columnspan=2, padx=25, pady=25)
b2.grid(column=1, row=4, columnspan=2, padx=25, pady=25)


root.mainloop()