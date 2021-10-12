import unittest

from classes import Session, MatchStatus
from ..helpers import compare_teams_weight

""" 
name : TestSession
description: Test the Generation of list
"""
class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = Session()

    def test_match_irregular_add_player(self):
        """Test match irregular add player
        Act : We try to add a player in a current game while teams are irregular
        Assert : The added player should be in the team with the least players.
        """
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
        """Test match category add player
        Act: We try to add a player in a current game with teams near to a category change.
        Assert : The added player should be in the team with the most experience.
        """
        # Setup our match
        players = self.session.retrieve_players('./src/tests/fixtures/dataTest.csv')
        self.session.prepare_players(players, [])
        self.session.match.start_game()
        # Add players
        self.session.add_player('John Doe', 66, 10)
        self.session.add_player('Erik Carlsberg', 68, 3)
        self.session.add_player('Test User', 71)
        # We check that the teams have still the same category
        # Meaning the new player has been added to the team with the less experience in order
        # To do not create a category switch
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
        self.session.prepare_players(players, [1,2,3,4,5,6])
        self.session.match.start_game()
        self.assertEqual(self.session.match.status, MatchStatus.IN_PROGRESS, "The actual match should be in progress")
        self.assertEqual(len(self.session.past_matches), 0, "There should be no past matches.")
        self.session.end_game()
        self.assertEqual(self.session.match.status, MatchStatus.FINISHED, "The actual match should be ended")
        self.assertEqual(len(self.session.past_matches), 1, "There should be one past match.")

    
    def test_match_add_player_experience(self):
        """Test to add a player to the less experienced team
        Act: We try to add a player to a match
        Assert : The added player should end up in less experienced group
        """
        # Retrieve players of same average weigth category but different experience
        # We setup our match
        players = self.session.retrieve_players('./src/tests/fixtures/dataTest.csv')
        self.session.prepare_players(players, [])
        # We then start the match
        self.session.match.start_game()
        # John doe 66kg and 10 years of experience
        # Erik Carlsberg 68kg and 3 years of experience
        self.session.add_player('John Doe', 66, 10)
        self.session.add_player('Erik Carlsberg', 68, 3)
        # We add a player Test User with 6 years of experience during the match
        self.session.add_player('Test User', 76, 6)
        # We check that the second team is longer due to Test User being added to the less experienced team
        self.assertEqual(len(self.session.match.first_team.players), 1, "first team should possess one member")
        self.assertEqual(len(self.session.match.second_team.players), 2, "Second team should possess two members")
        self.assertEqual(self.session.match.first_team.players[0].name, "John Doe", "John Doe should be in the first team")
        self.assertEqual(self.session.match.second_team.players[1].name, "Test User", "The new user should be in the second team")