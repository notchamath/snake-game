from turtle import Turtle

# This is 20 because that is the height and width of each sq that makes up the snake_body
MOVE_DISTANCE = 20

# Directions given by the turtle module
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(3):
            self.make_new_segment((i * -MOVE_DISTANCE, 0))

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].goto(self.snake_body[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def grow(self):
        self.make_new_segment(self.head.pos())

    def make_new_segment(self, position):
        body_segment = Turtle("square")
        body_segment.color("white")
        body_segment.penup()
        self.snake_body.append(body_segment)

        body_segment.goto(position)
