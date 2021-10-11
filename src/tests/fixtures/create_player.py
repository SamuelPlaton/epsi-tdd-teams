import random
from classes import Player
from faker import Faker

def create_player():
    """ create_player
    Return a player generated from random values
    :return a player object
    """
    fake = Faker()
    id = random.randint(10000, 99999)
    name = fake.name()
    weight = random.randint(50, 100)
    experience = random.randint(0, 40)
    player = Player(id, name, weight, experience)
    return player

def create_players(count = 1):
    """ create_players
    Return an array of players generated from random values
    :parameter count    the numbers of players to generated (int).
    :return an array of players
    """
    players = []
    i = 0
    while i < count:
        newPlayer = create_player()
        players.append(newPlayer)
        i = i + 1
    return players
