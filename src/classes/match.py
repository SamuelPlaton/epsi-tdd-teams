from functions import generate_teams, determine_category
from .team import Team
from enum import Enum

""" Enum Match Status
The Match status
"""
class MatchStatus(Enum):
    NOT_STARTED = 'not_started'
    PREPARATION = 'preparation',
    IN_PROGRESS = 'in_progress',
    FINISHED = 'finished',

"""
Class: Match

Description: Our class used to manage a match.

"""
class Match:

    def __init__(self):
        """ constructor
        Setup our empty object.
        """
        self.first_team = None
        self.second_team = None
        self.status = MatchStatus.NOT_STARTED

    def prepare_game(self, players):
        """ prepare_game
        Prepare our game with the default players.
        :parameter an array of players, we must have at least 1 player at the beginning
        """
        if len(players) > 0:
            self.status = MatchStatus.PREPARATION
            self.generate_teams(players)

    def start_game(self):
        """ start_game
        Start our game
        """
        if self.status == MatchStatus.PREPARATION:
            self.status = MatchStatus.IN_PROGRESS


    def end_game(self):
        """ start_game
        End our game
        """
        if self.status == MatchStatus.IN_PROGRESS:
            self.status = MatchStatus.FINISHED

    def add_player(self, player):
        """ add_player
        Add a player to the most convenient team
        :parameter player   A player object
        """
        # The game must be in preparation or have started
        if self.status != MatchStatus.PREPARATION and self.status != MatchStatus.IN_PROGRESS:
            return False
        # add player in team depending on the team size
        if len(self.first_team.players) < len(self.second_team.players):
            self.first_team.append_player(player)
            return self.first_team.name
        elif len(self.first_team.players) > len(self.second_team.players):
            self.second_team.append_player(player)
            return self.second_team.name
        # if teams have the same sizes, add player in team depending on the categories changes
        team_1_category = determine_category(sum(p.weight for p in self.first_team.players) / len(self.first_team.players))
        team_2_category = determine_category(sum(p.weight for p in self.second_team.players) / len(self.second_team.players))
        team_1_new_category = determine_category((sum(p.weight for p in self.first_team.players) + player.weight) / (len(self.first_team.players) + 1))
        team_2_new_category = determine_category((sum(p.weight for p in self.second_team.players) + player.weight) / (len(self.second_team.players) + 1))
        if team_1_category != team_1_new_category:
            self.second_team.append_player(player)
            return self.second_team.name
        elif team_2_category != team_2_new_category:
            self.first_team.append_player(player)
            return self.first_team.name
        # if categories does not change, add player in team depending on the experience
        team_1_experience = sum(p.weight for p in self.first_team.players)
        team_2_experience = sum(p.weight for p in self.second_team.players)
        if (team_1_experience < team_2_experience):
            self.first_team.append_player(player)
            return self.first_team.name
        else:
            self.second_team.append_player(player)
            return self.second_team.name



    def generate_teams(self, players):
        """generate_teams
        Generate two balanced teams from players given in parameter and attribute then to the match teams.
        :parameter players An Array of players
        """
        [first_players, second_players] = generate_teams(players)
        first_team = Team("1", first_players)
        second_team = Team("2", second_players)
        self.first_team = first_team
        self.second_team = second_team