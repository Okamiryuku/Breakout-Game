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
ball = Ball()

# Player Scoreboard
player_1 = ScoreBoard(0)


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
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddle) < 50 and ball.xcor() > 320 or ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() < -380:
        player_1.increase_score()
        ball.reset_position()

screen.exitonclick()