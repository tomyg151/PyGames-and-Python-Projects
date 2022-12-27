from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    # TODO: build init func, create the turtle player
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto_beginning()
        self.setheading(90)

    # TODO: build a move function so the player could move while press a keyboard
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # TODO: after player get to the top of the screen he get back to the beginning spot
    def goto_beginning(self):
        self.goto(STARTING_POSITION)  # go to the bottom of the screen in the middle


