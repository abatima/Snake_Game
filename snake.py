from turtle import Turtle


class Snake:
    def __init__(self):
     self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
     self.snake_parts = []
     for position in self.starting_positions:
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
        self.snake_parts[0].fd(20)