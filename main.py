from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def turn_counter_clockwise():
    tim.left(10)


def turn_clockwise():
    tim.right(10)


actions = {'w': move_forward, 's': move_backward, 'a': turn_counter_clockwise, 'd': turn_clockwise}

screen.listen()
for action in actions:
    screen.onkey(key=action,fun=actions[action])

screen.exitonclick()
