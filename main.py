import time
import turtle as t

from colors import BG_COLOR
from food import Food
from scoreboard import ScoreBoard
from snake import Snake


def end_game():
    global game_is_on
    game_is_on = False


screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor(BG_COLOR)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# When user enters spacebar, game ends
screen.onkey(key="space", fun=end_game)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.15)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) <= 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    # Detect collision with wall
    x, y = snake.head.xcor(), snake.head.ycor()
    if x > 280 or x < -280 or y > 280 or y < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with it's tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


t.done()
