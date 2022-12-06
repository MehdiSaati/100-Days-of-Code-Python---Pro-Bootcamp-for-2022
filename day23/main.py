from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(600, 600)
screen.title("Race Turtle")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20 :
            game_is_on = False
            scoreboard.game_over()
    #detect successful crossing 
    if player.is_at_finish_line():
        
        player.go_to_start()
        car_manager.leve_up()
        scoreboard.increase_level()


screen.exitonclick()