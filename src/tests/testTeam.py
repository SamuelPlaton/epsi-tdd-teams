from classes.Team import Team
from classes.Player import Player
import unittest

from .fixtures import createPlayer

class TeamTestMethods(unittest.TestCase):

    def test_create_team(self):
        firstTeam = Team()
        secondTeam = Team()
        self.assertEqual(type(firstTeam), Team, "firstTeam entity is not a Team")
        self.assertEqual(type(secondTeam), Team, "secondTeam entity is not a Team")
        self.assertEqual(firstTeam.name, None, "first team name must be Null")
        self.assertEqual(secondTeam.name, None, "second team name must be Null")
        self.assertEqual(firstTeam.players, None, "first team players' list must be Null")
        self.assertEqual(secondTeam.players, None, "second team players' list must be Null")
        
    def test_add_player(self):
        player = createPlayer()
        firstTeam = Team()
        firstTeam.players = []
        firstTeam.players.append(player)
        self.assertEqual(firstTeam.players[0], player, "firstTeam players first entity is not correct")