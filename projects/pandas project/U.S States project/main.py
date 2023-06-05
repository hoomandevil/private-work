import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    user_input = screen.textinput(title="Guess the State", prompt="Write a state name / Exit").capitalize()
    if user_input == "Exit":
        quit()
    if user_input in state_list:
        guessed_states.append(user_input)
        frag = turtle.Turtle()
        frag.hideturtle()
        frag.penup()
        state_data = data[data.state == user_input]
        frag.goto(int(state_data.x), int(state_data.y))
        frag.write(state_data.state.item()) #taking first item from index

screen.exitonclick()
