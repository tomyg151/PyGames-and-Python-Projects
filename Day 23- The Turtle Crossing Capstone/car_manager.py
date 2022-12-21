from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.all_cars_cord = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # TODO: Cars are randomly generated along the y-axis and will move from the right
    #  edge of the screen to the left edge.
    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=2, stretch_len=1)
            new_car.penup()
            new_car.setheading(270)
            new_car.goto(300,
                         random.randint(-250, 250))  # cars appears randomly on the y-axis on the right of the screen
            self.all_cars.append(new_car)

    # TODO: move the cars
    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    def get_all_car_coordinates(self):
        for car in self.all_cars:
            pos = car.position()
            self.all_cars_cord.append(pos)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
