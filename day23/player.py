from turtle import Turtle

START_pOSITION = (0, -280)
MOVE_DISTANCE = 10
FINSH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_to_start()
    def go_up(self):
        self.forward(MOVE_DISTANCE)
    
    def go_to_start(self):
        self.goto(START_pOSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINSH_LINE_Y :
            return True
        else:
            return False

