# Turtle Challenge 4 Draw a Random Walk
from turtle import Turtle, Screen
import random
color = ["aquamarine", "CornflowerBlue", "IndianRed", "DarkOrchid", "green", "red", "yellow", "black" ,"DeepSkyBlue", "LightSeaGreen", "SeaGreen"]
directions = [0, 90, 180, 270]
mehdi_the_turtle = Turtle()
mehdi_the_turtle.pensize(5)
mehdi_the_turtle.speed("fastest")
def random_walk(angle):
    mehdi_the_turtle.forward(10)
    mehdi_the_turtle.setheading(angle)

while True:
    mehdi_the_turtle.color(random.choice(color))
    rand_angle = random.choice(directions)
    random_walk(rand_angle)

my_screen = Screen()
my_screen.exitonclick()

