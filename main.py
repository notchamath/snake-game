from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
snake_body = []

for i in range(3):
    body_segment = Turtle("square")
    body_segment.color("white")
    body_segment.setpos(x=i*-20, y=0)

    snake_body.append(body_segment)


screen.exitonclick()
