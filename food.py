import random
import turtle as t

from colors import FOOD_COLOR


class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color(FOOD_COLOR)
        self.speed(0)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        """Refreshes the position of the food at a random location"""
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
