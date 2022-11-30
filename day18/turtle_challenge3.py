# Turtle Challenge 3 Draw Shapes
from turtle import Turtle, Screen
import random
color = ["aquamarine", "CornflowerBlue", "IndianRed", "DarkOrchid", "green", "red", "yellow", "black" ,"DeepSkyBlue", "LightSeaGreen", "SeaGreen"]
mehdi_the_turtle = Turtle()

def draw_shape(num_sides):
   angle = 360 / num_sides
   for _ in range(num_sides):
        mehdi_the_turtle.forward(100)
        mehdi_the_turtle.right(angle)
    
for num_sides in range (3, 10):
    rand_color = random.choice(color)
    mehdi_the_turtle.color(rand_color)
    draw_shape(num_sides)

my_screen = Screen()
my_screen.exitonclick()

