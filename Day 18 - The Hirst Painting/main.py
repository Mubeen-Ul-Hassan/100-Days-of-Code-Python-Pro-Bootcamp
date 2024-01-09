import turtle
import random


#  Extract rgb values using colorgram module and covert that values has hexadecimal values.
bright_colors = [
    "#FF5733",  # Vivid Orange
    "#FFC300",  # Vivid Yellow
    "#FF00FF",  # Vivid Magenta
    "#00FFFF",  # Cyan
    "#FF6699",  # Vivid Pink
    "#00FF00",  # Lime Green
    "#FF4500",  # OrangeRed
    "#FFD700",  # Gold
    "#7FFFD4",  # Aquamarine
    "#FF1493",  # Deep Pink
    "#9400D3",  # DarkViolet
    "#32CD32",  # LimeGreen
    "#00FF7F",  # SpringGreen
    "#FF8C00",  # DarkOrange
    "#8A2BE2",  # BlueViolet
    "#FFA07A",  # LightSalmon
    "#00FA9A",  # MediumSpringGreen
    "#FF00FF",  # Fuchsia
    "#1E90FF",  # DodgerBlue
    "#FFD700"   # Gold
]



# Turtle
    
# ----> Turtle position
turtle.teleport(-200,-200)
turtle.penup()
turtle.hideturtle()

turn = 0
for _ in range(10):
    for count in range(10):
        turtle.dot(20, random.choice(bright_colors))
        if count == 9:
            if turn == 0:
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turn = 1
            elif turn == 1:
                turtle.right(90)
                turtle.forward(50)
                turtle.right(90)
                turn = 0
        else:
            turtle.forward(50)

turtle.exitonclick()
turtle.exitonclick()