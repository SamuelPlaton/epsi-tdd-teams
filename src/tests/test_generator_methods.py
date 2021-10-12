import unittest
from classes import Generator,Player


class test_generator_methods(unittest.TestCase):
    def setUp(self):
        self.generator = Generator('./src/tests/fixtures/dataTest.csv')
        self.PlayerList = self.generator.generate_players()

    def test_player_generator_output_is_a_list(self):
        self.assertEqual(isinstance(self.PlayerList,list), True, 'Function need to generate a list')

    def test_player_generator_output_is_a_player_list(self):
        only_player = True
        for elem in self.PlayerList:
            if type(elem) != Player:
                only_player = False
                pass
        self.assertEqual(only_player, True, 'Function need to generate a Player\'s list')

    def test_count_player_generated(self):
        self.assertEqual(self.generator.count_player_list(), 20, 'The list need to generate all the players')