import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
from bricks import Brick
from game_over import GameOver


# Window Setup
screen = Screen()
screen.setup(width=800, height=1200)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Calling classes
paddle = Paddle((0, -550))
ball = Ball((0, -525))
game_over = GameOver()

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
    if ball.ycor() > 585:
        ball.bounce_y()

    if ball.xcor() > 385 or ball.xcor() < -385:
        ball.bounce_x()

    if ball.distance(paddle) < 20:
        ball.paddle_bounce()

    if ball.ycor() < -600:
        game_over.game_over_check(ball=ball)


screen.exitonclick()
