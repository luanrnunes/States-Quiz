import turtle
import pandas

screen = turtle.Screen()
screen.title("QUIZ - ESTADOS DOS E.U.A")

image = "blank_states_img.gif"

turtle.addshape(image)
turtle.shape(image)

#Para pegar as coordenadas de clique na tela e ajustar na apresentacao dos nomes
# def get_mouse_click_coord(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coord)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
missing_states = []


while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Estados Corretos",
                                    prompt="Digite o nome dos estados").title()

    if answer_state == "Exit" or answer_state == "Sair" or answer_state == "Save":
        missing_states = [state for state in all_states if state not in guessed_states]
        # if answer_state == "Exit" or answer_state == "Sair" or answer_state == "Save":
        #     for state in all_states:
        #         if state not in guessed_states:
        #             missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)

        new_data.to_csv("states_to_learn.csv")
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.color("black")
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    # if all_states in guessed_states:
    #     states_to_learn = pandas.DataFrame(all_states)
    #     states_to_learn.remove(guessed_states)
    #     #states_to_learn.to_csv("states_to_learn.csv")
    #     print(states_to_learn)

turtle.mainloop()

