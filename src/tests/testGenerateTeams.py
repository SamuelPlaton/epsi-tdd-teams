import unittest

from src import generateTeams


class TestGenerateTeams(unittest.TestCase):
    def test_generate_empty_team(self):
        [firstTeam, secondTeam] = generateTeams([])
        self.assertEqual("1", "2")
        #self.assertEqual(firstTeam.length, secondTeam.length)
