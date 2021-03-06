from csv import reader
from classes import Player
from datetime import datetime

"""
Class: Generator

Description: Generate the players from csv.

"""
class  Generator:
    def __init__(self, file_path_csv):
        """ constructor
        Setup the generator.
        :parameter file_path_csv   The file path For the generation of the players

        """
        self.file_path_csv = file_path_csv
        self.list = []


    def generate_players(self):
        """ generate_players
        :return the player list generated from the csv.
        """
        datenow = int(datetime.today().strftime('%Y'))
        with open(self.file_path_csv, 'r') as read_obj:
            csv_reader = reader(read_obj)
            pass_first_line=True
            i = 1
            for row in csv_reader:
                if pass_first_line==True:
                    pass_first_line=False
                else:
                    elems=row[0].split(';')
                    self.list.append(Player(i,elems[0]+" "+elems[1],int(elems[2]),datenow - int(elems[3])))
                    i += 1
        return self.list

    def count_player_list(self):
        """ count_player_list
        :return the length of the list.
        """
        return len(self.list)


