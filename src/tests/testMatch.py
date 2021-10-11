from classes.Match import Match
import unittest

class MatchTestMethods(unittest.TestCase):

    def test_create_match(self):
        partie = Match()
        self.assertEqual(type(partie), Match, "created entity is not a Match")
        self.assertEqual(partie.firstTeam, None, "first team must be Null")
        self.assertEqual(partie.secondTeam, None, "second team must be Null")