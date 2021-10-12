"""
Class: Match

Description: Our class used to manage a match.

"""
from functions import generate_teams
from enum import Enum

class MatchStatus(Enum):
    NOT_STARTED = 'not_started'
    PREPARATION = 'preparation',
    IN_PROGRESS = 'in_progress',
    FINISHED = 'finished',

class Match:

    def __init__(self):
        """ constructor
        Setup our empty object.
        """
        self.first_team = None
        self.second_team = None
        self.status = MatchStatus.NOT_STARTED

    def prepare_game(self):
        self.status = MatchStatus.PREPARATION

    def start_game(self):
        self.status = MatchStatus.IN_PROGRESS

    def end_game(self):
        self.status = MatchStatus.FINISHED

    def add_player(self, player):
        return 0

    def generate_teams(self, players):
        """generate_teams
        Generate two balanced teams from players given in parameter and attribute then to the match teams.
        :parameter players An Array of players
        """
        [first_team, second_team] = generate_teams(players)
        self.first_team = first_team
        self.second_team = second_team