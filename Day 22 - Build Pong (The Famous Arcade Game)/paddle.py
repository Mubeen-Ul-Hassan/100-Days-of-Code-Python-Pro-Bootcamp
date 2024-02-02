from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.color('white')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle()
        
    def paddle(self):
        self.goto(self.position)

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 50
        else:
            new_y = self.ycor()
        self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 50
        else:
            new_y = self.ycor()
        self.goto(self.xcor(), new_y)