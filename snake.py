from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create()
        self.snake_head = self.snake_parts[0]

    def create(self):
     for position in STARTING_POSITIONS:
         new_snake_part = Turtle("square")
         new_snake_part.color("white")
         new_snake_part.penup()
         new_snake_part.goto(position)
         self.snake_parts.append(new_snake_part)

    def move(self):
        for snake_part_number in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[snake_part_number - 1].xcor()
            new_y = self.snake_parts[snake_part_number - 1].ycor()
            self.snake_parts[snake_part_number].goto(new_x, new_y)
        self.snake_head.fd(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)


