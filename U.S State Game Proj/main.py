import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S STATE GAME")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# # print the x y cordinates of the click location on the map
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

correct_state = []

while len(correct_state) < 50:
    # user guess
    answer_state = screen.textinput(title=f"Score {len(correct_state)}/50", prompt="What's another state's name                         ").title()

    data = pandas.read_csv("50_states.csv")

    # list of state
    states_list = data.state.to_list()
    if answer_state == "Exit":
        missing_state = []
        for state in states_list:
            if state not in correct_state:
                missing_state.append(state)
        data_squirrel = pandas.DataFrame(missing_state)
        data_squirrel.to_csv("missing_state.csv")
        break


    # check if the user guess among the 50 states
    if answer_state in states_list:

        correct_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # coordinates of state on map
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())


# states_to_learn.csv



