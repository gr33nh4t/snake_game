from turtle import Turtle
import random

class Food(Turtle):
    def init(self):
        super().init()
        # Set up the food object with the circle shape
        self.shape('circle')
        self.color('red')
        self.shapesize(0.5,0.5)
        self.penup()
        self.appear()

    def appear(self):
        # Randomly position the food on the screen
        food_x = random.randint(-230, 230)
        food_y = random.randint(-230, 230)
        self.goto(food_x, food_y)