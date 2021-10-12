"""
Our main file application.
"""

from classes import Match, MatchStatus
from classes import Player
import numpy as np

if __name__ == '__main__':
    match = Match()
    start = "n"
    players = [Player('1', 'John', 65, 80), Player('2', 'David', 65, 80), Player('3', 'Erik', 65, 80)]
    while (match.status == MatchStatus.NOT_STARTED):
        print('Bienvenue dans le generateur de match')
        prepare = input('Souhaitez-vous demarrer ? o/n ')
        if prepare == "o":
            # Here retrieve players from CSV
            print('Voici les joueurs disponibles :')
            for index, player in enumerate(players):
                print(index,': ', player.name)
            print('Quels joueurs souhaitez-vous sélectionner ?')
            # Retrieve selected players indexes
            string_indexes = input('*Entrez leur numeros au format 1,2,3 : ');
            list_indexes = string_indexes.split(',')
            int_list_indexes = []
            for index in list_indexes:
                int_list_indexes.append(int(index))
            formatted_players = np.array(players)
            selected_players = formatted_players[int_list_indexes]
            match.prepare_game(selected_players)
        match.start_game()
        print('La partie demarre !')
        print("Voici la composition de l'equipe ", match.first_team.name, ":")
        for p in match.first_team.players:
            print(p.name, p.weight, "kg", p.experience, "annees d'experience")
        print("Voici la composition de l'equipe ", match.second_team.name, ":")
        for p in match.second_team.players:
            print(p.name, p.weight, "kg", p.experience, "annees d'experience")

