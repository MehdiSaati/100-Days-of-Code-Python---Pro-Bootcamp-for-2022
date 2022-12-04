from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 240)
        self.write(f"{self.l_score} ", align="center", font=("Arial", 25, "normal"))
        self.goto(50, 240)
        self.write(f"{self.r_score}", align="center", font=("Arial", 25, "normal"))


    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
 

 