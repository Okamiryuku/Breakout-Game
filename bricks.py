from turtle import Turtle


class Brick(Turtle):

    def __init__(self, paddle_pos):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(paddle_pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def delete_brick(self):
        pass
