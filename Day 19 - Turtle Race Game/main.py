from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    tim.left(10)
    move_forward()

def move_right():
    tim.right(10)
    move_forward()

def clear_screen():
    tim.reset()

screen.listen()

screen.onkey(key="w", fun=move_forward) # w == to move forward
screen.onkey(key="s", fun=move_backward) # s == to move backward
screen.onkey(key="a", fun=move_left) # a == to move counterclock wise
screen.onkey(key="d", fun=move_right) # d == to move clockwise
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()