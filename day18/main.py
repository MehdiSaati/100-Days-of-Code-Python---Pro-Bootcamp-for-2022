# Hirst Painting Project
# import colorgram
import turtle as turtle_module
import random
# rgb_colors = []
# colors = colorgram.extract('image.hpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(236, 248, 243), (36, 95, 183), (236, 165, 79), (244, 223, 87), (215, 69, 105), (98, 197, 234),                (250, 51, 22), (203, 70, 21), (240, 106, 143), (185, 47, 90), (143, 233, 216), (252, 136, 166),                (165, 175, 233), (66, 45, 13), (72, 205, 170), (83, 187, 100), (20, 156, 51), (24, 36, 86), (252, 220, 0),                (164, 28, 8), (105, 39, 44), (250, 152, 2), (22, 151, 229), (108, 213, 249), (254, 12, 3), (38, 48, 98),                (98, 96, 186)]
tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")

tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(150)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(10, random.choice(color_list))
    tim.fd(25)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(25)
        tim.setheading(180)
        tim.fd(250)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()