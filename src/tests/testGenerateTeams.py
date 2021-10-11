import unittest

from functions import generateTeams
from functions import determineCategory
from .fixtures import createPlayers

class TestGenerateTeams(unittest.TestCase):
    def setUp(self):
        self.players = createPlayers(20)

    def test_generate_team(self):
        [firstEmptyTeam, secondEmptyTeam] = generateTeams([])
        self.assertEqual(len(firstEmptyTeam), len(secondEmptyTeam), "Both teams must have the same size")
        self.assertEqual(len(firstEmptyTeam), 0, "Teams must be empty")
        [firstTeam, secondTeam] = generateTeams(self.players)
        self.assertEqual(len(firstTeam), len(secondTeam), "Both teams must have the same size")
        self.assertEqual(len(firstTeam), 10, "Each team must have half of the players")
        self.assertEqual(len(firstTeam) + len(secondTeam), 20, "Each player must be in a team")
        firstTeamWeight = 0
        secondTeamWeight = 0

        for player in firstTeam:
            firstTeamWeight = firstTeamWeight + player.weight

        for player in secondTeam:
            secondTeamWeight = secondTeamWeight + player.weight

        firstTeamCategory = determineCategory(firstTeamWeight/len(firstTeam))
        secondTeamCategory = determineCategory(secondTeamWeight/len(secondTeam))
        self.assertEqual(firstTeamCategory, secondTeamCategory, "Teams average must be in the same category")




