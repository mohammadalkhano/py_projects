class Player:

    def __init__(self, name, score):
        self.player_name = name
        self.player_score = score

    def __str__(self):
        return f"The player is {self.name} and it's score is {self.score}"
        #return self()
