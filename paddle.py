from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.setposition(position)

    def go_up(self):
        # moves the paddle up changing its Y position
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        # moves the paddle down changing its Y position
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
