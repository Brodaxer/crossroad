import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(random.randint(-100,800), random.randint(-240, 290))
        self.shapesize(stretch_len=1.5)
        self.setheading(180)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
        if self.xcor() < -300:
            self.goto((random.randint(300,800), random.randint(-240, 290)))



