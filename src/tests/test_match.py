from classes import Match
from .fixtures import create_players
from functions import determine_category

import unittest

""" 
name : TestMatch
description: Test the Match class and it's methods
"""
class TestMatch(unittest.TestCase):
    def setUp(self):
        """Arrange our tests with random players"""
        self.players = create_players(20)

    def test_create_match(self):
        """Create an empty match"""
        match = Match()
        self.assertEqual(type(match), Match, "created entity is not a Match")
        self.assertEqual(match.first_team, None, "first team must be Null")
        self.assertEqual(match.second_team, None, "second team must be Null")

    def test_generate_empty_teams(self):
        """Setup empty teams in a match"""
        match = Match()
        # Assert on an empty list of players
        match.generate_teams([])
        self.assertEqual(len(match.first_team), len(match.second_team), "Both teams must have the same size")
        self.assertEqual(len(match.first_team), 0, "Teams must be empty")

    def test_generate_filled_teams(self):
        """Setup balanced teams in a match"""
        match = Match()
        # Assert on a random list of 20 players
        match.generate_teams(self.players)
        self.assertEqual(len(match.first_team), len(match.second_team), "Both teams must have the same size")
        self.assertEqual(len(match.first_team), int(len(self.players)/2), "Each team must have half of the players")
        self.assertEqual(len(match.first_team) + len(match.second_team), len(self.players), "Each player must be in a team")

        # Retrieve teams weight
        first_team_weight = sum(p.weight for p in match.first_team)
        second_team_weight = sum(p.weight for p in match.second_team)
        # Determine their category
        first_team_category = determine_category(first_team_weight / len(match.first_team))
        second_team_category = determine_category(second_team_weight / len(match.second_team))
        # Assert that they are on the same category
        self.assertEqual(first_team_category, second_team_category, "Teams average must be in the same category")