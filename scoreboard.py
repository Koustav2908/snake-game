import turtle as t

from colors import SCORE_COLOR

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color(SCORE_COLOR)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.display_score()

    def display_score(self):
        """Displays the current score of gamer at the top"""
        self.clear()
        self.write(
            f"SCORE = {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        """Increases the score by one"""
        self.score += 1
        self.display_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))

        self.score = 0
        self.display_score()
