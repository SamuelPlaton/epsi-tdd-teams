"""
Class: Team

Description: Our class team.

"""
class Team:
    def __init__(self, name, players = []):
        """ constructor
        Setup our team.
        :parameter name     The team name (string)
        :parameter players  An array of players
        """
        self.name = name
        self.players = players

    def append_player(self, player):
        """ append_player
        append a player to the team.
        :parameter player   The player to add to the team
        """
        self.players.append(player)
