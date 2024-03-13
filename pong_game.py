from turtle import Turtle, Screen
from paddle_class import Paddle
from title_class import Title
from ball_class import Ball
from scoreboard_class import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

title = Title()
ball = Ball()
scoreboard = Scoreboard()

left_paddle = Paddle((-350, 0))

right_paddle = Paddle((350, 0))

screen.listen()

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")



game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()
    
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()
        

    if ball.xcor() > 370:
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        left_paddle.goto(-350,0)
        right_paddle.goto(350,0)
        ball.reset_position()
        
    if ball.xcor() < -370:
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        right_paddle.goto(350,0)
        left_paddle.goto(-350,0)
        ball.reset_position()
        




screen.exitonclick()