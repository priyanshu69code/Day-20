from turtle import Turtle, Screen
import time
import random
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

color = [
    (238, 238, 238),  # Gainsboro
    (211, 211, 211),  # Light Gray
    (192, 192, 192),  # Silver
    (169, 169, 169),  # Dark Gray
    (128, 128, 128),  # Gray
    (105, 105, 105),  # Dim Gray
    (0, 0, 0),        # Black
    (255, 255, 255),  # White
    (245, 245, 220),  # Beige
    (220, 220, 220),  # Light Grey
    (128, 128, 0),    # Olive
    (128, 128, 128),  # Grey
    (210, 180, 140),  # Tan
    (255, 228, 181),  # Moccasin
    (255, 250, 205),  # Lemon Chiffon
    (255, 239, 213),  # Papaya Whip
    (255, 245, 238),  # Seashell
    (245, 245, 245),  # White Smoke
    (240, 240, 240),  # Gray 97
    (128, 128, 128),  # Grey
    (47, 79, 79),     # Dark Slate Grey
    (105, 105, 105),  # Dim Grey
    (95, 158, 160),   # Cadet Blue
    (210, 210, 210),  # Light Grey
    (216, 191, 216),  # Thistle
    (119, 136, 153),  # Light Slate Grey
    (220, 220, 220),  # Gainsboro
    (211, 211, 211),  # Light Gray
    (192, 192, 192),  # Silver
    (169, 169, 169)   # Dark Gray
]


class Snake:
    def __init__(self,):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for i in range(3):
            block = Turtle("square")
            block
            block.color(random.choice(color))
            block.penup()
            block.goto(i*(-20), 0)
            self.blocks.append(block)

    def add_blocks(self, poss):
        block = Turtle("square")
        block.color(random.choice(color))
        block.penup()
        block.goto(poss)
        self.blocks.append(block)

    def extend(self):
        self.add_blocks(self.blocks[-1].position())

    def move(self):
        for block in range(len(self.blocks) - 1, 0, -1):
            newx = self.blocks[block - 1].xcor()
            newy = self.blocks[block - 1].ycor()
            self.blocks[block].goto(newx, newy)
        self.head.forward(20)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
