from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position_tuple):
        super().__init__()
        self.paddle_position = position_tuple
        self.create_paddle(self.paddle_position)

    def create_paddle(self, start_position_tuple):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(start_position_tuple)

    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)

