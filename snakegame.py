from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("Black")
screen.setup(height=600, width=600)
screen.title("This is My snake game")

blocks = []
screen.tracer(0)

for i in range(3):

    block = Turtle("square")
    block.color("white")
    block.penup()
    block.goto(i*(-20), 0)
    blocks.append(block)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    for block in range(len(blocks) - 1, 0, -1):
        newx = blocks[block - 1].xcor()
        newy = blocks[block - 1].ycor()
        blocks[block].goto(newx, newy)
    blocks[0].forward(20)
    blocks[0].left(90)


screen.exitonclick()
