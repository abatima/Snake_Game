from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
test = Turtle()

class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create()

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
        self.snake_parts[0].fd(MOVE_DISTANCE)

    def up(self):
        self.snake_parts[0].setheading(90)

    def down(self):
        self.snake_parts[0].setheading(270)

    def left(self):
        self.snake_parts[0].setheading(180)

    def right(self):
        self.snake_parts[0].setheading(0)


