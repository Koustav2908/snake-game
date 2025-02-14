import turtle as t

from colors import SNAKE_COLOR

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20

DIRECTIONS = {
    "RIGHT": 0,
    "UP": 90,
    "LEFT": 180,
    "DOWN": 270,
}


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Initializes the snake body"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment to the snake body"""
        new_segment = t.Turtle(shape="square")
        new_segment.penup()
        new_segment.color(SNAKE_COLOR)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extends the snake body by adding one additional segment to it's tail"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake in a straight line"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Press the 'up' arrow key to go upwards"""
        if self.head.heading() != DIRECTIONS["DOWN"]:
            self.head.setheading(DIRECTIONS["UP"])

    def down(self):
        """Press the 'down' arrow key to go downwards"""
        if self.head.heading() != DIRECTIONS["UP"]:
            self.head.setheading(DIRECTIONS["DOWN"])

    def left(self):
        """Press the 'left' arrow key to go towards left"""
        if self.head.heading() != DIRECTIONS["RIGHT"]:
            self.head.setheading(DIRECTIONS["LEFT"])

    def right(self):
        """Press the 'right' arrow key to go towards right"""
        if self.head.heading() != DIRECTIONS["LEFT"]:
            self.head.setheading(DIRECTIONS["RIGHT"])
