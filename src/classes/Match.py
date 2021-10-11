from functions import generate_teams

class Match:

    def __init__(self):
        self.first_team = None
        self.second_team = None

    def generate_teams(self, players):
        [first_team, second_team] = generate_teams(players)
        self.first_team = first_team
        self.second_team = second_team