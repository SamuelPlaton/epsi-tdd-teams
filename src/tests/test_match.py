from classes import Match, MatchStatus, Player
from .fixtures import create_player, create_players
from .helpers import compare_teams_weight

import unittest

""" 
name : TestMatch
description: Test the Match class and it's methods
"""
class TestMatch(unittest.TestCase):
    def setUp(self):
        """Arrange our tests with random players"""
        
        self.players = create_players(20)
        self.player = create_player()

    def test_create_match(self):
        """Create a match"""
        match = Match()
        self.assertEqual(type(match), Match, "created entity is not a Match")
        self.assertEqual(match.first_team, None, "first team must be Null")
        self.assertEqual(match.second_team, None, "second team must be Null")
        self.assertEqual(match.status, MatchStatus.NOT_STARTED, "Match must not have started")

    def test_prepare_match(self):
        """Prepare a match"""
        match = Match()
        # Check that the game is prepared with players
        match.prepare_game(self.players)
        self.assertEqual(match.status, MatchStatus.PREPARATION, "Match must be in preparation")
        self.assertEqual(len(match.first_team.players) + len(match.second_team.players), len(self.players), "Match must have teams settled")

    def test_start_match(self):
        """Start a match"""
        match = Match()
        # Check that a match must be prepared before
        match.start_game()
        self.assertEqual(match.status, MatchStatus.NOT_STARTED, "Match must be prepared before")
        # Check that the match is in progress
        match.prepare_game(self.players)
        match.start_game()
        self.assertEqual(match.status, MatchStatus.IN_PROGRESS, "Match must be in progress")

    def test_end_game(self):
        """End a match"""
        match = Match()
        # Check that a match must be in progress before
        match.end_game()
        self.assertEqual(match.status, MatchStatus.NOT_STARTED, "Match must be in progress before")
        match.prepare_game(self.players)
        match.end_game()
        self.assertEqual(match.status, MatchStatus.PREPARATION, "Match must be in progress before")
        match.start_game()
        match.end_game()
        self.assertEqual(match.status, MatchStatus.FINISHED, "Match must be finished")

    def test_generate_teams(self):
        """Setup balanced teams in a match"""
        match = Match()
        # Assert on an empty list of players
        match.generate_teams([])
        self.assertEqual(len(match.first_team.players), len(match.second_team.players), "Both teams must have the same size")
        self.assertEqual(len(match.first_team.players), 0, "Teams must be empty")
        # Assert on a random list of 20 players
        match.generate_teams(self.players)
        self.assertEqual(len(match.first_team.players), len(match.second_team.players), "Both teams must have the same size")
        self.assertEqual(len(match.first_team.players) + len(match.second_team.players), len(self.players), "Each player must be in a team")
        # Assert that they are on the same category
        self.assertTrue(compare_teams_weight(match.first_team, match.second_team), "Teams average must be in the same category")

    def test_uneven_match_add_player(self):
        """Add a player and make sure he is added to the most convenient team"""
        # Check that the added player is prioritized depending on the teams sizes
        inequal_match = Match()
        inequal_match.prepare_game([Player('1', 'A', 65, 80), Player('2', 'B', 68, 20), Player('3', 'C', 68, 20)])
        self.assertNotEqual(len(inequal_match.first_team.players), len(inequal_match.second_team.players),
                            "Teams must not be the same size")
        inequal_match.add_player(self.player)
        self.assertEqual(len(inequal_match.first_team.players), len(inequal_match.second_team.players),
                         "Teams must now be the same size")

    def test_add_player(self):
        # Check that we must be at least in preparation to add a new player
        match = Match()
        match.add_player(self.player)
        self.assertEqual(match.first_team, None, "Match must be at least in preparation to add a new player")
        # Check that the added player is then prioritized depending on the category switch
        preprocessed_players = [Player('1', 'Player 1', 65, 40), Player('2', 'Player 2', 68, 20)]
        match.prepare_game(preprocessed_players)
        # Check that both teams are on the same category
        self.assertTrue(compare_teams_weight(match.first_team, match.second_team), "Teams average must be in the same category")
        # Add a new player
        match.add_player(Player('3', 'Player 3', 71, 5))
        # Check that teams categories still did not switch categories
        # Meaning the player is added to the team with the most experience in order to do not switch categories
        self.assertTrue(compare_teams_weight(match.first_team, match.second_team), "Teams average must be in the same category")
        # Add a new player to test to make a 2v2
        match.add_player(Player('4', 'Player 4', 65, 0))
        # Check now that a new player is added to the less experimented team
        first_team_experience = sum(p.experience for p in match.first_team.players)
        second_team_experience = sum(p.experience for p in match.second_team.players)
        if first_team_experience < second_team_experience:
            less_experimented_team = "1"
        else:
            less_experimented_team = "2"
        match.add_player(Player('5', 'Player 5', 65, 40))
        # check that the player is added to the less experimented team and the values switched
        if less_experimented_team == "1":
            self.assertTrue(sum(p.experience for p in match.first_team.players) > sum(p.experience for p in match.second_team.players),
                            "The team experience advantage must have switched")
        else:
            self.assertTrue(sum(p.experience for p in match.second_team.players) > sum(p.experience for p in match.first_team.players),
                            "The team experience advantage must have switched")





