# Turtle Challenge 4 Draw a Random Walk
from turtle import Turtle, Screen
import random
# color = ["aquamarine", "CornflowerBlue", "IndianRed", "DarkOrchid", "green", "red", "yellow", "black" ,"DeepSkyBlue", "LightSeaGreen", "SeaGreen"]
directions = [0, 90, 180, 270]
mehdi_the_turtle = Turtle()
mehdi_the_turtle.pensize(5)
mehdi_the_turtle.speed("fastest")
mehdi_the_turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

def random_walk(angle):
    mehdi_the_turtle.forward(10)
    mehdi_the_turtle.setheading(angle)

while True:
    # mehdi_the_turtle.color(random.choice(color))
    mehdi_the_turtle.color(random_color())
    rand_angle = random.choice(directions)
    random_walk(rand_angle)

my_screen = Screen()
my_screen.exitonclick()

