from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # reverses the direction
        self.y_move *= -1

    def bounce_x(self):
        # reverses the direction
        self.x_move *= -1
        # increases the speed of the ball when it touches the left of right parts
        self.move_speed *= 0.8

    def reset(self):
        self.goto(0, 0)
        # resets speed to initial
        self.move_speed = 0.1
        # starts bouncing
        self.bounce_x()
