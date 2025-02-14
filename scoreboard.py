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
        self.display_score()

    def display_score(self):
        """Displays the current score of gamer at the top"""
        self.clear()
        self.write(f"SCORE = {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score by one"""
        self.score += 1
        self.display_score()

    def game_over(self):
        """Prints 'Game Over' to the screen"""
        self.goto(0, 0)
        self.write("⚔ GAME OVER ⚔", align=ALIGNMENT, font=FONT)
