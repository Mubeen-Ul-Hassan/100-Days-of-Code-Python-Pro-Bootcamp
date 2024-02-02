from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('orange')
        self.penup()
        self.shapesize(1, 1)
        self.shape('circle')
        self.x_move = 35
        self.y_move = 35

    def move(self):
        cord_x = self.xcor() + self.x_move
        cord_y = self.ycor() + self.y_move
        self.goto(cord_x, cord_y)
    
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()