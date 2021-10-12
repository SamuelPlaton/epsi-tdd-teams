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
    """
        
    """
    def test_match_pending_players (self):
        # Retrieve our 9 players from csv then start our match
        players = self.session.retrieve_players('./src/tests/fixtures/dataTest.csv')
        self.session.prepare_players(players, [1, 2, 3, 4, 5, 6, 7, 8, 9,10])

        self.session.match.start_game()
        first_team_before=self.session.match.first_team.players
        second_team_before=self.session.match.second_team.players
        self.session.add_pending_player('EL BOBBY', 20)
        self.session.add_pending_player('EL SECOND BOBBY', 30)
        #look if team haven't change
        self.assertEqual(len(first_team_before), len(self.session.match.first_team.players),
                         "Teams should have the same amount of players")
        self.assertEqual(len(second_team_before), len(self.session.match.second_team.players),
                         "Teams should have the same amount of players")
        self.session.match.end_game()
        #Create a new match
        self.session.prepare_players(players, [1, 2, 3, 4, 5, 6, 7, 8, 9,10])

        self.session.match.start_game()
        #Look if one of the two player have been added to the first team
        find = False
        for elem in self.session.match.first_team.players:
            if elem.name == 'EL SECOND BOBBY' or elem.name == "EL BOBBY":
                find = True
        self.assertTrue(find,'EL Booby sould be here')
        #Look if one of the two player have been added to the second team

        find = False
        for elem in self.session.match.second_team.players:
            if elem.name == "EL SECOND BOBBY" or elem.name == "EL BOBBY":
                find = True
        self.assertTrue(find,'EL  Booby sould be here')
        self.assertNotEqual(len(first_team_before), len(self.session.match.first_team.players),
                         "Teams should have the same amount of players")
        self.assertNotEqual(len(second_team_before), len(self.session.match.second_team.players),
                         "Previous team and current team should not have the same amount of players")
        self.session.match.end_game()
        self.session.end_game()
