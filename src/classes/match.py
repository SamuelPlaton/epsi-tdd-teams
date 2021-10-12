"""
Class: Match

Description: Our class used to manage a match.

"""
from functions import generate_teams, determine_category
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

    def prepare_game(self, players):
        if len(players) > 0:
            self.status = MatchStatus.PREPARATION
            self.generate_teams(players)

    def start_game(self):
        if self.status == MatchStatus.PREPARATION:
            self.status = MatchStatus.IN_PROGRESS


    def end_game(self):
        if self.status == MatchStatus.IN_PROGRESS:
            self.status = MatchStatus.FINISHED

    def add_player(self, player):
        if self.status != MatchStatus.PREPARATION and self.status != MatchStatus.IN_PROGRESS:
            return False
        # add player in team depending on the team size
        if len(self.first_team) < len(self.second_team):
            self.first_team.append(player)
            return True
        elif len(self.first_team) > len(self.second_team):
            self.second_team.append(player)
            return True
        # add player in team depending on the category switch
        team_1_category = determine_category(sum(p.weight for p in self.first_team) / len(self.first_team))
        team_2_category = determine_category(sum(p.weight for p in self.second_team) / len(self.second_team))
        team_1_new_category = determine_category((sum(p.weight for p in self.first_team) + player.weight) / (len(self.first_team) + 1))
        team_2_new_category = determine_category((sum(p.weight for p in self.second_team) + player.weight) / (len(self.second_team) + 1))
        if team_1_category != team_1_new_category:
            self.second_team.append(player)
            return True
        elif team_2_category != team_2_new_category:
            self.first_team.append(player)
            return True
        # add player depending on experience
        team_1_experience = sum(p.weight for p in self.first_team)
        team_2_experience = sum(p.weight for p in self.second_team)
        if (team_1_experience < team_2_experience):
            self.first_team.append(player)
            return True
        else:
            self.second_team.append(player)
            return True



    def generate_teams(self, players):
        """generate_teams
        Generate two balanced teams from players given in parameter and attribute then to the match teams.
        :parameter players An Array of players
        """
        [first_team, second_team] = generate_teams(players)
        self.first_team = first_team
        self.second_team = second_team