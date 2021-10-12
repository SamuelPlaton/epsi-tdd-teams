import unittest
from unittest.mock import patch

from classes import Session
from ..helpers import compare_teams_weight

""" 
name : TestSession
description: Test the Generation of list
"""
class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = Session()

    def test_match_irregular_add_player(self):
        # Retrieve our 9 players from csv then start our match
        players = self.session.retrieve_players('./src/tests/fixtures/dataTest.csv')
        self.session.prepare_players(players, [1,2,3,4,5,6,7,8,9])
        # We start our match
        # We check that the teams have the same category but not the same amount of players
        self.assertNotEqual(len(self.session.match.first_team.players), len(self.session.match.second_team.players),
                            "Teams should not have the same amount of players")
        self.assertTrue(compare_teams_weight(self.session.match.first_team, self.session.match.second_team),
                            "Teams should be in the same category")
        # We add a player
        self.session.add_player('John Doe', 70)
        # We check that the teams have still the same category and the same amount of players
        self.assertEqual(len(self.session.match.first_team.players), len(self.session.match.second_team.players),
                            "Teams should have the same amount of players")
        self.assertTrue(compare_teams_weight(self.session.match.first_team, self.session.match.second_team),
                        "Teams should be in the same category")

    def test_match_category_add_player(self):
        # Retrieve players close to a category evolution
        # John doe 66kg and 10 years of experience
        # Erik Carlsberg 68kg and 3 years of experience
        players = self.session.retrieve_players('./src/tests/fixtures/dataTest.csv')
        self.session.prepare_players(players, [20, 21])
        self.session.match.start_game()
        # We add a player Test User of 70kg
        self.session.add_player('Test User', 70)
        # We check that the teams have still the same category
        # Meaning the new player has been added to the team with the less experience in order
        # To do not create a category switch
        self.assertTrue(compare_teams_weight(self.session.match.first_team, self.session.match.second_team),
                        "Teams should be in the same category")

