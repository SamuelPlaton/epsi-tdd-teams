from classes import Team
from .fixtures import create_player

import unittest


""" 
name : TestTeam
description: Test the Team class and it's methods
"""
class TestTeam(unittest.TestCase):

    def test_create_team(self):
        """Test team creation"""
        team = Team("Test name", [])
        self.assertEqual(team.name, "Test name", "Team name must be filled by the construction")
        self.assertEqual(len(team.players), 0, "Team players must be empty at the creation")
        
    def test_add_player(self):
        """Test team player addition"""
        player = create_player()
        team = Team("Test name")
        team.append_player(player)
        self.assertEqual(team.players[0], player, "Team player must be added")