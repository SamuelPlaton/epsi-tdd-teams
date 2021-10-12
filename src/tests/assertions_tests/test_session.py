import unittest
from unittest.mock import patch

from classes import Session

""" 
name : TestSession
description: Test the Generation of list
"""
class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = Session()

    @patch('classes.session.Session.greetings_input', return_value='o')
    @patch('classes.session.Session.prepare_players_input', return_value='1,2,3,4,5')
    @patch('classes.session.Session.process_game_input', return_value='1')
    def test_match_irregular_add_player(self, input, input2, input3):
        self.session.greetings()
        self.session.prepare_players()
        self.session.match.start_game()
        self.session.print_prompt()
        # On vérifie les données de la session
        self.assertEqual(len(self.session.match.first_team), len(self.session.match.second_team))
