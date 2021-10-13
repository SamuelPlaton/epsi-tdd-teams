import unittest

from classes import Session, MatchStatus, Player
from ..helpers import compare_teams_weight

""" 
name : TestSession
description: Test the Session
"""
class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = Session()

    def test_match_uneven_add_player(self):
        """Test match uneven add player
        Act : We try to add a player in a current game while teams are uneven.
        Assert : The added player should be in the team with the least players.
        """
        # Setup uneven teams
        players = self.session.retrieve_players('./src/tests/fixtures/dataTest.csv')
        self.session.prepare_players(players, [1,2,3,4,5,6,7,8,9])
        # Check that teams are uneven and still in the same category
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

        # Setup a new match
        self.session.match.end_game()
        self.session.prepare_players(players, [1, 2, 3, 4, 5, 6, 7, 8, 9,10])
        self.session.match.start_game()
        #Look if one of the two player have been added to one of the teams
        first_user_found = False
        second_user_found = False
        for player in [*self.session.match.first_team.players, *self.session.match.second_team.players]:
            if player.name == 'Pending User 1':
                first_user_found = True
            elif player.name == "Pending User 2":
                second_user_found = True
        self.assertTrue(first_user_found and second_user_found, 'Both users must have been foud')

    def test_match_category_add_player(self):
        """Test match category add player
        Act: We try to add a player in a current game with teams near to a category change.
        Assert : The added player should be in the team with the most experience.
        """
        # Setup our match
        players = self.session.retrieve_players('./src/tests/fixtures/dataTest.csv')
        self.session.prepare_players(players, [])
        self.session.match.start_game()
        self.session.add_player('John Doe', 66, 10)
        self.session.add_player('Erik Carlsberg', 68, 3)
        # Check that the new player addition did not provoked a category switch
        self.session.add_player('Test User', 71)
        self.assertTrue(compare_teams_weight(self.session.match.first_team, self.session.match.second_team),
                        "Teams should be in the same category")
        # Test User is added in the team with the most experience because else it would change the second team category
        self.assertEqual(self.session.match.first_team.players[0].name, "John Doe", "John Doe should be in the first team")
        self.assertEqual(self.session.match.first_team.players[1].name, "Test User", "The new user should be in the first team")

    def test_end_match(self):
        """Test to end a match
        Act: We try to start a match then end it.
        Assert : The match should be ended and saved in the session past matches
        """
        players = self.session.retrieve_players('./src/tests/fixtures/dataTest.csv')
        self.session.prepare_players(players, [1, 2, 3, 4, 5, 6])
        self.session.match.start_game()
        self.assertEqual(self.session.match.status, MatchStatus.IN_PROGRESS, "The actual match should be in progress")
        self.assertEqual(len(self.session.past_matches), 0, "There should be no past matches.")
        self.session.end_game()
        self.assertEqual(self.session.match.status, MatchStatus.FINISHED, "The actual match should be ended")
        self.assertEqual(len(self.session.past_matches), 1, "There should be one past match.")


