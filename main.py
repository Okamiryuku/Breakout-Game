import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
from bricks import Brick


# Window Setup
screen = Screen()
screen.setup(width=800, height=1200)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Calling classes
paddle = Paddle((0, -550))
ball = Ball((0, -530))

# Player Scoreboard
scoreboard = ScoreBoard(0)


# Registering Commands
screen.listen()
screen.onkeypress(paddle.move_right, "d")
screen.onkeypress(paddle.move_left, "a")


# Running the Game
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 580 or ball.ycor() < -580:
        ball.bounce()

    if ball.xcor() > 350 or ball.xcor() < -350:
        ball.bounce()


screen.exitonclick()
