from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_hs()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"SCORE: {self.score} | HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_hs()

        self.score = 0
        self.refresh_score()

    def get_hs(self):

        with open("data.txt") as data:
            hs = int(data.read())
            self.high_score = hs

    def set_hs(self):
        with open("data.txt",  mode="w") as data:
            data.write(f"{self.high_score}")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)
