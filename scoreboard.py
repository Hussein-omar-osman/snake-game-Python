from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.score = 0
        with open('data.txt') as data:
            self.highestScore = int(data.read())
        self.write(arg=f'Score: {self.score}', align='center', font=('Arial', 17, 'bold'))
        self.hideturtle()

    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def finished(self):
        self.goto(0, 0)
        self.write(arg=f'Game Over', align='center', font=('Arial', 17, 'bold'))

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.highestScore}', align='center', font=('Arial', 17, 'bold'))

    def reset(self):
        if self.score > self.highestScore:
            self.highestScore = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.highestScore}')

        self.score = 0
        self.update_scoreboard()
