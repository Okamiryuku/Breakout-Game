import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
from bricks import Brick
import random

# Window Setup
screen = Screen()
screen.setup(width=800, height=1200)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Calling classes
paddle = Paddle((0, -550))
ball = Ball((0, -525))
list_bricks = []  # My list of Bricks Objects

# Set the initial position for the first line of bricks
y_pos = 400
brick_count = 14  # Number of bricks in a row
total_width = 800  # Total width for the row

# Calculate the fixed distance between bricks
brick_width = total_width / brick_count

# Loop to create multiple rows of bricks
for _ in range(7):
    x_pos = -380
    for _ in range(brick_count):
        # Generate a random width for the brick
        random_width = random.uniform(0.5, 2.8)
        wall = Brick((x_pos, y_pos), random_width)
        list_bricks.append(wall)
        x_pos += brick_width
    y_pos -= 50

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

    if ball.distance(paddle) < 40:
        ball.paddle_bounce()

    if ball.ycor() < -600:
        scoreboard.game_over()

    if len(list_bricks) == 0:
        scoreboard.win()

    for brick in list_bricks:
        if ball.distance(brick) < 30:
            ball.brick_bounce()
            brick.delete_brick()
            list_bricks.remove(brick)
            print(list_bricks)

screen.exitonclick()
