import unittest
from classes import Generator,Player

""" 
name : testGenerator
description: Test the Generation of list
"""
class testGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = Generator('./src/tests/fixtures/dataTest.csv')
        self.player_list = self.generator.generate_players()



    def test_player_generator_output_is_a_list(self):
        """Test list generation """
        #Test if the generated list is a list
        self.assertEqual(isinstance(self.player_list, list), True, 'Function need to generate a list')
        only_player = True
        for elem in self.player_list:
            if type(elem) != Player:
                only_player = False
                pass
        #Test if the generated list is a list of Player
        self.assertEqual(only_player, True, 'Function need to generate a Player\'s list')

    def test_count_player_generated(self):
        """Test number of generated items"""
        #assert if the 20 player from the test list have een generated
        self.assertEqual(self.generator.count_player_list(), 20, 'The list need to generate all the players')