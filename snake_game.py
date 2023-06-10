from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

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

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # Detect collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 \
        or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            score_board.reset()
            snake.reset()



screen.exitonclick()