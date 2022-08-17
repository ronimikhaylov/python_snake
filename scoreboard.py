

class Scoreboard():
    def __init__(self):
        self.score = 0

    def update(self, score):
        self.score += score

    def display(self):
        print("Score: {}".format(self.score))   

    def game_over(self):
        print("Game Over")
        print("Final Score: {}".format(self.score))

    def increase_score(self):
        self.score += 1
        self.display()
    
