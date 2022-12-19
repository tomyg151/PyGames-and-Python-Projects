from turtle import Screen
import time
from Snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # Write the user score on the bord
        score.add_to_score()
    # if the segment come to the wall throw the segment to the other side of the screen
    if snake.head.xcor() > 290:
        snake.head.goto(-290, snake.head.ycor())
    elif snake.head.xcor() < -290:
        snake.head.goto(290, snake.head.ycor())
    elif snake.head.ycor() > 290:
        snake.head.goto(snake.head.xcor(), -290)
    elif snake.head.ycor() < -290:
        snake.head.goto(snake.head.xcor(), 290)
    # Detect collision with tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
    # if head collides with any segment in the tail:
    # trigger game_over

screen.exitonclick()
