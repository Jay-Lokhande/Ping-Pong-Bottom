from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("#F5765B")
screen.setup(width=800, height=600)
screen.title("Ping Pong From Bottom")
screen.tracer(0)

x = Turtle()
x.penup()
x.hideturtle()
x.color('black')
x.goto(-130, 200)
x.write("Made by Jay", font=('Courier', 30, 'italic'))

b_paddle = Paddle((0, -250))
ball = Ball()
scoreboard = Scoreboard()

paddle_big = Turtle()
paddle_big.shape("square")
paddle_big.color("#C7F55B")
paddle_big.shapesize(stretch_wid=1, stretch_len=38)
paddle_big.penup()
paddle_big.goto((0, 250))


screen.listen()
screen.onkey(b_paddle.go_left, "Left")
screen.onkey(b_paddle.go_right, "Right")
screen.onkey(b_paddle.size_big, "Up")
screen.onkey(b_paddle.size_small, "Down")


x = True
while x:
    time.sleep(ball.move_speed)
    screen.update()
    ball.moven()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.distance(b_paddle) < 50 and ball.ycor() < -220 or ball.distance(paddle_big) < 380 and ball.ycor() > 220:
        ball.bounce_y()

    if ball.ycor() < -300:
        ball.reset_position()
        scoreboard.b_point()

    if ball.ycor() > 300:
        ball.reset_position()


screen.exitonclick()
