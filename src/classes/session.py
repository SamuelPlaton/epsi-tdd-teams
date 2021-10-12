"""
Class: Session

Description: Our class session.

"""
from .match import Match
from .player import Player
from .generator import Generator
from functions import determine_category

from enum import Enum
import numpy as np

class SessionStatus(Enum):
    OFF = "off"
    ON = "on"

class Session:
    def __init__(self):
        """ constructor
        Setup our session.
        :parameter match            Our current match
        :parameter past_matches     An array of our past matches
        :parameter status           The status of our session (ON/OFF)
        :parameter pending_players  An array of players waiting for the next game
        """
        self.match = Match()
        self.past_matches = []
        self.status = SessionStatus.ON
        self.pending_players = []

    def launch(self):
        """ launch
        Our session activity
        """
        # Keep doing until our session stopped
        while self.status == SessionStatus.ON:
            self.match = Match()
            self.greetings()
            self.prepare_players()
            self.process_game()

    def greetings(self):
        """ greetings
        Greets our user
        """
        print('\nBienvenue dans le generateur de match\n')
        start = "n"
        while start != "o":
            start = self.greetings_input()

    def greetings_input(self):
        return input('Souhaitez-vous demarrer ? o/n\n')

    def prepare_players(self):
        """ prepare_players
        Retrieve players from our CSV
        Ask the user to select the ones he want
        Add them to the next game with the pending players
        """
        # Retrieve players from our CSV file
        generator = Generator('./public/data.csv')

        players = generator.generate_players()
        # Display them
        print('\nVoici les joueurs disponibles :')
        for index, player in enumerate(players):
            print(index, ': ', player.name)
        # Ask the user for which ones he is interested in
        print('\nQuels joueurs souhaitez-vous sélectionner ?')
        # Retrieve selected players indexes
        string_indexes = self.prepare_players_input()
        list_indexes = string_indexes.split(',')
        int_list_indexes = []
        for index in list_indexes:
            int_list_indexes.append(int(index))
        formatted_players = np.array(players)
        selected_players = formatted_players[int_list_indexes]
        # Prepare the game with the selected players and the pending ones
        self.match.prepare_game([*selected_players, *self.pending_players])
        self.pending_players = []

    def prepare_players_input(self):
        return input('*Entrez leur numeros au format 1,2,3 :\n')

    def process_game(self):
        """ process_game
        Start the match and process it
        """
        # Start match and display teams
        self.match.start_game()
        self.display_team(self.match.first_team)
        self.display_team(self.match.second_team)
        print('\n\nLa partie demarre !\n\n')
        # Our command panel
        command = None
        while command != "4" and command != "5":
            command = self.print_prompt()

    def print_prompt(self):
        print('1 ** Afficher les equipes')
        print('2 ** Ajouter un joueur a la partie en cours')
        print("3 ** Ajouter un joueur a la partie d'apres")
        print('4 ** Relancer une nouvelle partie')
        print('5 ** Fermer la session')
        command = self.process_game_input()
        if command == '1':
            self.display_team(self.match.first_team)
            self.display_team(self.match.second_team)
        elif command == '2':
            self.add_player()
        elif command == '3':
            self.add_pending_player()
        elif command == '4':
            self.end_game()
        elif command == '5':
            self.status = SessionStatus.OFF
        return command

    def process_game_input(self):
        return input('\nEntrez une option : ')

    def add_player(self):
        """ add_player
        Add a player to the current game
        """
        [name, weight] = self.add_player_input()
        team_added = self.match.add_player(Player('', name, weight, 0))
        print("Joueur ajoute a l'equipe ", team_added, '\n')

    def add_pending_player(self):
        """ add_player
        Add a player for the next game
        """
        [name, weight] = self.add_player_input()
        self.pending_players.append(Player('', name, weight, 0))
        print("Joueur ajoute pour la prochaine partie\n")

    def add_player_input(self):
        name = input('\nVeuillez entrer un nom de joueur :\n')
        weight = int(input('Veuillez entrer le poids du joueur :\n'))
        return [name, weight]

    def display_team(self, team):
        """ display_team
        Display a team and it's information
        :parameter team     The team object
        """
        weight = sum(p.weight for p in team.players) / len(team.players)
        experience = sum(p.experience for p in team.players) / len(team.players)
        print("\n\nVoici la composition de l'equipe ", team.name, ":\n")
        print('Categorie :', determine_category(weight))
        print('Poids moyen :', round(weight, 2), 'kg')
        print('Experience moyenne :', round(experience, 2), 'ans\n')
        for p in team.players:
            print(p.name, p.weight, "kg", p.experience, "annees d'experience")

    def end_game(self):
        """ end_game
        End the game
        """
        self.match.end_game()
        self.past_matches.append(self.match)
        print('\n\nFin du match\n\n')
