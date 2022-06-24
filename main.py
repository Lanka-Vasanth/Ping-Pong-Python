from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.bgcolor("black")
screen.screensize(800,600)
screen.title("Pong")
screen.tracer(0)
r_pad=Paddle((350,0))
l_pad=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()
screen.listen()

gameOn=True
screen.onkey(r_pad.go_up,"Up")
screen.onkey(r_pad.go_down,"Down")
screen.onkey(l_pad.go_up,"w")
screen.onkey(l_pad.go_down,"s")
while gameOn:
    time.sleep(0.015)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bouncewall()
    
    if ball.distance(r_pad)<50 and ball.xcor()>320 or ball.distance(l_pad)<50 and ball.xcor()<-320:
        ball.bouncepaddle()
    if ball.xcor()>390:
        ball.new()
        scoreboard.lpoint()

    if ball.xcor()<-390:
        ball.new()
        scoreboard.rpoint()

screen.exitonclick()
