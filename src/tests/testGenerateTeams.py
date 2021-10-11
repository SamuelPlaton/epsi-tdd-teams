import unittest

from functions import generateTeams
from functions import determineCategory
from .fixtures import createPlayers


##
# name: TestGenerateTeams
#
# description :
# Unit Tests of team generation
##
class TestGenerateTeams(unittest.TestCase):
    # Arrange our tests
    def setUp(self):
        self.players = createPlayers(40)

    # Act: test team generation from an array of players
    def test_generate_team(self):
        # Assert on an empty list of players
        [first_empty_team, second_empty_team] = generateTeams([])
        self.assertEqual(len(first_empty_team), len(second_empty_team), "Both teams must have the same size")
        self.assertEqual(len(first_empty_team), 0, "Teams must be empty")
        # Assert on a random list of 40 players
        [first_team, second_team] = generateTeams(self.players)
        self.assertEqual(len(first_team), len(second_team), "Both teams must have the same size")
        self.assertEqual(len(first_team), 20, "Each team must have half of the players")
        self.assertEqual(len(first_team) + len(second_team), 40, "Each player must be in a team")

        # Retrieve teams weight
        first_team_weight = sum(p.weight for p in first_team)
        second_team_weight = sum(p.weight for p in second_team)
        # Determine their category
        first_team_category = determineCategory(first_team_weight / len(first_team))
        second_team_category = determineCategory(second_team_weight / len(second_team))
        # Assert that they are on the same category
        self.assertEqual(first_team_category, second_team_category, "Teams average must be in the same category")
