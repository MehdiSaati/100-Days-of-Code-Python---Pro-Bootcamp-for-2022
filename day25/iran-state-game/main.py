import turtle
import os
os.chdir("/Users/mahan/Desktop/100DaysOfCodePython-master/day25/iran-state-game")
import pandas

screen = turtle.Screen()
screen.title("استان های ایران")
image ="/Users/mahan/Desktop/100DaysOfCodePython-master/day25/iran-state-game/iran.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

guess_list = []
while len(guess_list) < 31:
    answer_guess = screen.textinput(title=f"{len(guess_list)} / 31 correct", prompt="Whats guess state?").title()
    data = pandas.read_csv("states.csv", encoding='utf8')
    all_states = data.state.to_list()

    if answer_guess == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guess_list:
                missing_state.append(state)
        df = pandas.DataFrame(missing_state)
        df.to_csv("states_to_learn.csv")


        break
    if answer_guess in all_states:
        guess_list.append(answer_guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_guess)

