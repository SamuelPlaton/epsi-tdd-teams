"""
Class: Match

Description: Our class used to manage a match.

"""
from functions import generate_teams

class Match:

    def __init__(self):
        """ constructor
        Setup our empty object.
        """
        self.first_team = None
        self.second_team = None

    def generate_teams(self, players):
        """generate_teams
        Generate two balanced teams from players given in parameter and attribute then to the match teams.
        :parameter players An Array of players
        """
        [first_team, second_team] = generate_teams(players)
        self.first_team = first_team
        self.second_team = second_team