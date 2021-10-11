import unittest
from classes import Generator,Player

class TestReaderMethods(unittest.TestCase):
    generator = Generator('./src/tests/fixtures/dataTest.csv')
    PlayerList = generator.generate_players()

    def test_Player_generator_output_is_a_list(self):
        self.assertEqual(isinstance(self.PlayerList,list), True, 'Function need to generate a list')

    def test_Player_generator_output_is_a_Player_list(self):
        only_player = True
        for elem in self.PlayerList:
            if type(elem) != Player:
                only_player = False
                pass
        self.assertEqual(only_player, True, 'Function need to generate a Player\'s list')

    def test_count_player_generated(self):
        self.assertEqual(self.generator.count_player_list(), 20, 'The list need to generate all the players')