from turtle import Turtle
import os 
# Get the current working directory
os.chdir(r"C:\Users\mahan\Desktop\100DaysOfCodePython-master\day24\snake_game")

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")
class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

        # self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} High Score : {self.high_score}" , align=ALIGNMENT, font=FONT)

    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

            
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1 
        self.update_scoreboard()


        