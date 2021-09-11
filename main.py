from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# sets up the main screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

# creates paddles, ball and score objects
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

# makes paddles respond to key presses
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    # slows down the ball
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detects collision with top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detects collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # detects when the right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset()
        score.left_point()

    # detect when the left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset()
        score.right_point()

screen.exitonclick()
