import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("LightBlue")
screen.title("The Turtle Crossing Capstone")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move()

    # player get to the top of the screen
    # detect when player pass the upper screen so he need to return to the beginning and get a point
    if player.ycor() >= 280:
        player.goto_beginning()  # go to the beginning of the screen(middle bottom)
        score.point()
        car_manager.level_up()

    # detect collision with the cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False




screen.exitonclick()