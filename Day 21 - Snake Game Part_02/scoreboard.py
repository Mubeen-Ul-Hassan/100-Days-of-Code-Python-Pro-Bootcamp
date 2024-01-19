from turtle import Turtle

# Score Adjustment
SCORE_ALIGNMENT = "center"
SCORE_FONT = ("Courier",16,"bold")

# Score Adjustment
LEVEL_ALIGNMENT = "left"
LEVEL_FONT = SCORE_FONT

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 0
        self.count = 5
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
        self.update_level()

    def game_over(self):
        self.goto(-50, 0)
        self.write("GAME OVER", font=LEVEL_FONT)

    def update_scoreboard(self):
        self.goto(-50, 270)
        self.write(f"Score: {self.score}", font=SCORE_FONT)

    def update_level(self):
        self.goto(-270, 270)
        self.write(f"Level: {self.level}", font=LEVEL_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def increase_level(self):
        if self.score == self.count:
            self.level += 1
            self.count += 5
        self.update_level()
    