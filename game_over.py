from turtle import Turtle


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.game_over = False
        self.message = "You lose"

    def show_message(self):
        self.clear()
        self.write(self.message, align="center", font=("Arial", 32, "bold"))

    def game_over_check(self, ball):
        if ball.ycor() < -600:
            self.game_over = True
            self.show_message()