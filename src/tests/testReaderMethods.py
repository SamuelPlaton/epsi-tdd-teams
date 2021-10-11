import unittest
from classes import Generator,Player

class TestReaderMethods(unittest.TestCase):
    generator = Generator('/src/tests/fixtures/dataTest.xlsx')
    def test_Player_generator_output(self):
        self.assertEqual(self.generator.generatePlayers(), list[Player],'Function need to generate a Player\'s list')
    def test_count_Player_generated(self):
        self.assertEqual(self.generator.countPlayerList(),20,'The list need to generate all the players')