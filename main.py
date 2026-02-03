import time
from turtle import Screen
from src.snake import Snake
from src.food import Food
from src.scoreboard import Scoreboard

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_head.distance(food) < 15:
        food.move_food()
        snake.extend_snake()
        scoreboard.increase_score()

    if (snake.snake_head.xcor() > 280
            or snake.snake_head.xcor() < -280
            or snake.snake_head.ycor() > 280
            or snake.snake_head.ycor() < -280
    ):
        scoreboard.reset()
        snake.reset()

    for snake_part in snake.snake_parts[2:]:
        if snake.snake_head.distance(snake_part) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
