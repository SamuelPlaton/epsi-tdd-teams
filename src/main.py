"""
Our main file application.
"""

from classes import Match, MatchStatus
from classes import Player

if __name__ == '__main__':
    match = Match()
    start = "n"
    while (match.status == MatchStatus.NOT_STARTED):
        print('Bienvenue dans le générateur de match')
        start = input('Souhaitez-vous démarrer ? o/n ')
        if start == "o":
            match.prepare_game()

    player1 = Player('1', 'John', 60, 10)
    player2 = Player('2', 'John 2', 60, 5)
    match.generate_teams([player1, player2])