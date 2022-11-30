# Turtle Challenge 2 - Draw Square by penup
from turtle import Turtle, Screen


mehdi_the_turtle = Turtle()

# draw line by black and white color

# def draw_line():
#     mehdi_the_turtle.color("red")
#     mehdi_the_turtle.forward(5)
#     mehdi_the_turtle.color("white")
#     mehdi_the_turtle.forward(5)
 
# for _ in range(4):
#     for _ in range(10):
#        draw_line()
#     mehdi_the_turtle.right(90)
#     draw_line()

# draw by pen up
for _ in range(4):
    for _ in range(10):
        mehdi_the_turtle.forward(10)
        mehdi_the_turtle.penup()
        mehdi_the_turtle.forward(10)
        mehdi_the_turtle.pendown()
    mehdi_the_turtle.right(90)




my_screen = Screen()
my_screen.exitonclick()

input(">")