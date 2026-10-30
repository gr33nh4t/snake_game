from turtle import Turtle
import random
import time

angles = (90, 0, 0, 0)

class Snake:
    def init(self):
        self.position = [(-40, 0), (-20, 0), (0, 0)]
        self.snakes = []
        # Create the snake
        self.create_snake()
        self.head = self.snakes[-1]
        

    def create_snake(self):
        for position in self.position:
            new_snake = Turtle()
            new_snake.penup()
            new_snake.shape('square')
            new_snake.color('white')
            new_snake.goto(position)

        # Use body gif shape for each segment
        new_snake.shape("square")
        self.snakes.append(new_snake)

    def move(self):
        for i in range(len(self.snakes) - 1):
            self.snakes[i].goto(self.snakes[i + 1].pos())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            

    def extend(self):
        new_segment = Turtle()
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(self.snakes[0].pos())
        self.snakes.insert(0, new_segment)