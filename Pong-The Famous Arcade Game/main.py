from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time  # To add delay in the movement of the ball

screen = Screen()  # Creating a screen object from Screen Class
screen.setup(width=800, height=600)
screen.bgcolor("black")  # setting the background colour of the screen
screen.title("My Ping-Pong Game")
screen.tracer(0)  # stop the animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()  # listens for the keyboard input
# right paddle moving
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
# left paddle moving
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True  # This is done to create a while loop

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()  # updates the screen and shows the animation which is removed by tracer(0)
    ball.move()  # calling a method from Ball Class
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce
        ball.bounce_y()
    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when ball pass the x_cor of the screen in the R paddle
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()

    # Detect when ball pass the x_cor of the screen in the L paddle
    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()

screen.exitonclick()
