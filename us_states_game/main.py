import turtle
import pandas
# from states import States

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# state = States()

score = 0
correct_states = []
# game_is_on = True

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

state = turtle.Turtle()
state.hideturtle()
state.penup()

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in states_list:
        x = int(data[data.state == answer_state].x)
        y = int(data[data.state == answer_state].y)
        state.goto(x, y)
        state.write(answer_state, align="center", font=("Courier", 10, "normal"))
        correct_states.append(answer_state)
        score = len(correct_states)

missing_states = [state for state in states_list if state not in correct_states]
# for state in states_list:
#     if state not in correct_states:
#         missing_states.append(state)
dict_missing_states = {"state": missing_states}
df = pandas.DataFrame(dict_missing_states)
df.to_csv("missing_states.csv")
