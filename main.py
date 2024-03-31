import time
import turtle

from food import Food
from snake import Snake
from scorecard import Score

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

time.sleep(2)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if (snake.snakeHead.xcor() > 290 or snake.snakeHead.ycor() > 290 or
            snake.snakeHead.ycor() < -290 or snake.snakeHead.xcor() < -300):
        score.game_over()
        game_is_on = False

    if snake.snakeHead.distance(food) < 15:
        snake.add_new_segment()
        food.change_position()
        score.increase()

    for segment in snake.segments[1:]:
        if segment.distance(snake.snakeHead) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()
        
