from csv import reader
from classes import Player
class  Generator:
    def __init__(self, file_path_csv):
        self.file_path_csv = file_path_csv
        self.list = []


    def generate_players(self):
        with open(self.file_path_csv, 'r') as read_obj:
            csv_reader = reader(read_obj)
            pass_first_line=True
            i = 1
            for row in csv_reader:
                if pass_first_line==True:
                    pass_first_line=False
                else:
                    elems=row[0].split(';')
                    self.list.append(Player(i,elems[0]+" "+elems[1],elems[2],elems[3]))
                    i += 1
        return self.list

    def count_player_list(self):
        return len(self.list)


