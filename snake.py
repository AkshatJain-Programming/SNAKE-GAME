import turtle


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snakeHead = self.segments[0]

    def create_snake(self):
        start_position = [(0, 0), (-20, 0), (-40, 0)]
        for position in start_position:
            new_segment = turtle.Turtle("square")
            new_segment.penup()
            new_segment.goto(position)
            new_segment.color("white")
            self.segments.append(new_segment)

    def add_new_segment(self):
        position = self.segments[-1].position()
        new_segment = turtle.Turtle("square")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color("white")
        self.segments.append(new_segment)

    def move(self):
        for seg_idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_idx - 1].xcor()
            new_y = self.segments[seg_idx - 1].ycor()
            self.segments[seg_idx].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.snakeHead.heading() != 270:
            self.snakeHead.setheading(90)

    def down(self):
        if self.snakeHead.heading() != 90:
            self.snakeHead.setheading(270)

    def left(self):
        if self.snakeHead.heading() != 0:
            self.snakeHead.setheading(180)

    def right(self):
        if self.snakeHead.heading() != 180:
            self.snakeHead.setheading(0)
