from turtle import Turtle

class Score_board(Turtle):
    def init(self):
        super().init()
        self.score = 0
        self.shape('classic')
        self.color('white')
        self.penup()
        self.goto(0,268)

        self.hideturtle()
        self.score_board()

    def score_board(self):
        self.write(f"Score: {self.score}", align='center', font=('Arial', 20, 'bold'))

    def update_score(self):
        self.score = self.score + 1
        self.clear()
        self.score_board()

    def game_over(self):
        self.goto(0,0)
        
        self.write(f"Game Over! \nFinal Score: {self.score}", align='center', font=('Arial', 30, 'bold'))