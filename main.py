from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Score
screen = Screen()
screen.bgcolor("Blue")
screen.setup(height=600, width=600)
screen.title("This is My Snake game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
# snake.create_snake()
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
game_over = True
# wall_boundary = [snake.head.xcor() > 295, snake.head.xcor(
# ) < -295, snake.head.ycor() > 295, snake.head.ycor() < -295]
while game_over:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refress()
        snake.extend()
        score.stack()

    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        # if any(wall_boundary):
        game_over = False
        score.wall_game_over()

    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 18:
            game_over = False
            score.wall_game_over()

screen.exitonclick()
