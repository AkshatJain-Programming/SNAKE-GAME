from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt", 'r') as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()

        self.goto(-70, 270)
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("aerial", 12, "bold"))

        self.goto(70, 270)
        self.write(arg=f"High Score: {self.high_score}", move=False, align="center", font=("aerial", 12, "bold"))

    def increase(self):
        self.goto(-70, 270)
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("aerial", 12, "bold"))

        if self.score > self.high_score:
            self.increase_high_score()

        self.goto(70, 270)
        self.write(arg=f"High Score: {self.high_score}", move=False, align="center", font=("aerial", 12, "bold"))

    def increase_high_score(self):
        self.high_score = self.score
        with open("high_score.txt", 'w') as file:
            file.write(f'{self.high_score}')

    def game_over(self):
        game_over = Turtle()
        game_over.penup()
        game_over.color("white")
        game_over.hideturtle()
        game_over.goto(0, 0)
        game_over.write(arg="Game Over", move=False, align="center", font=("aerial", 12, "bold"))
