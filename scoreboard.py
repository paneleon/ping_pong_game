from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        # updates the score for left paddle
        self.goto(-100, 220)
        self.write(self.left_score, align="center", font=("Courier", 60, "bold"))
        # updates the score for right paddle
        self.goto(100, 220)
        self.write(self.right_score, align="center", font=("Courier", 60, "bold"))

    def left_point(self):
        # increases score for left paddle
        self.left_score += 1
        self.update_score()

    def right_point(self):
        # increases score for right paddle
        self.right_score += 1
        self.update_score()
