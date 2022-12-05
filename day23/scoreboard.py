from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__( )
        self.hideturtle()
        self.penup()
        self.goto(-240, 270)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=("Courier", 15 , "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Courier", 30 , "bold"))

