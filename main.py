from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score_board
import time

# set up the screen
window = Screen()
window.setup(600, 600, 0, 0)
window.bgcolor('black')
window.title('Snake Game')

window.tracer(False)

instruction = Turtle()
snake = Snake()
food = Food()
score_game = Score_board()

# key buildings
window.listen()
window.onkey(snake.up, 'Up')
window.onkey(snake.down, 'Down')
window.onkey(snake.right, 'Right')
window.onkey(snake.left, 'Left')
window.onkey(snake.start_moving, 'space')

game_is_on = True
while game_is_on:
    window.update()
    time.sleep(0.1)
    

    if snake.head.distance(food) < 15:
        food.appear()
        snake.extend()
        score_game.update_score()

    for segment in snake.snakes[:-1]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            window.bgcolor("dark red")
            score_game.game_over()

    if snake.head.xcor() > 265 or snake.head.xcor() < -265 or snake.head.ycor() > 265 or snake.head.ycor() < -265:
        game_is_on = False
        window.bgcolor("dark red")
        score_game.game_over()


window.exitonclick()


