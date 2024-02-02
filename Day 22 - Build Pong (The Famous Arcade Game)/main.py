from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.bgcolor('black')
screen.setup(width=800, height=600)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")

screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 273 or ball.ycor() < -273:
        ball.bounce_y()
    
    # Detect collision with right_paddle
    if ball.distance(right_paddle) < 45 and ball.xcor() > 320 or ball.distance(left_paddle) < 45 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()