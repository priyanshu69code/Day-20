from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed(0)
        self.refress()

    def refress(self):
        ran_x = random.randint(-280, 280)
        ran_y = random.randint(-280, 280)
        self.goto(ran_x, ran_y)
