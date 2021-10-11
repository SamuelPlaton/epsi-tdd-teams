import random
from classes import Player
from faker import Faker

def create_player():
    fake = Faker()
    id = random.randint(10000, 99999)
    name = fake.name()
    weight = random.randint(50, 100)
    experience = random.randint(0, 40)
    player = Player(id, name, weight, experience)
    return player

def create_players(count = 1):
    players = []
    i = 0
    while i < count:
        newPlayer = create_player()
        players.append(newPlayer)
        i = i + 1
    return players
