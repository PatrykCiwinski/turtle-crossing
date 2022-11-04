import turtle
from turtle import*

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-70, 260)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Level {self.score}", "bolder", font=("Verdena",16))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(-70,0)
        self.write("GAME OVER", font=("Verdena",16))
