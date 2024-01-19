from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.increase_level()

screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) # By changing value of sleep you can decrease or increase speed of snake
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 17: # Distance from snake head to food.
        scoreboard.increase_score()
        scoreboard.increase_level()
        snake.extend()
        food.refresh()
    
    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()

# snake class
# score class
# scoreboard class