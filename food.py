from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()

        new_x = random.randint(-280, 280)
        new_y = random.randint(-260, 260)
        self.goto(new_x, new_y)

    def change_position(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-260, 260)
        self.goto(new_x, new_y)
