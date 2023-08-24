from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake_body = []
is_game_on = True

for i in range(3):
    body_segment = Turtle("square")
    body_segment.color("white")
    body_segment.penup()
    body_segment.goto(x=i*-20, y=0)

    snake_body.append(body_segment)

while is_game_on:
    screen.update()
    time.sleep(0.1)

    for i in range(len(snake_body)-1, 0, -1):
        snake_body[i].goto(snake_body[i-1].pos())
    snake_body[0].forward(20)

screen.exitonclick()
