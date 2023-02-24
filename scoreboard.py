from turtle import Turtle


class Score(Turtle):
    def __init__(self,):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score {self.score}", align="center",
                   font=("Arial", 16, "normal"))

    def stack(self):
        self.clear()
        self.score += 1
        self.write(f"Score {self.score}", align="center",
                   font=("Arial", 16, "normal"))

    def wall_game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center",
                   font=("Arial", 16, "normal"))