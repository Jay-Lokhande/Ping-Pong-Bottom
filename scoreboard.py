from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.b_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, -50)
        self.write(self.b_score, align="center", font=("Courier", 80, "normal"))

    def b_point(self):
        self.b_score += 1
        self.update_scoreboard()
