from turtle import Turtle
import random

COLORS = ["red", "green", "blue", "yellow", "purple" ]
STARTING_MOVE_DISANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISANCE = 5

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            rand_y = random.randint(-250, 250)
            new_car.goto(280, rand_y )
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    
    def leve_up(self):
        self.car_speed += MOVE_INCREMENT