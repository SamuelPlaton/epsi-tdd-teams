"""
Our main file application.
"""

from classes import match
from classes import player
if __name__ == '__main__':
    start = "n"
    while (start != "o"):
        print('Bienvenue dans le générateur de match')
        start = input('Souhaitez-vous démarrer ? o/n ')

    match = match()
    player1 = player('1', 'John', 60, 10)
    player2 = player('2', 'John 2', 60, 5)
    match.generate_teams([player1, player2])


