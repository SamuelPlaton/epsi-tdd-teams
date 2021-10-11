import random
from classes import Player
from faker import Faker

def createPlayer():
    fake = Faker()
    id = random.randint(10000, 99999)
    name = fake.name()
    weight = random.randint(45, 120)
    experience = random.randint(0, 40)
    player = Player(id, name, weight, experience)
    return player

def createPlayers(count = 1):
    players = []
    i = 0
    while i < count:
        newPlayer = createPlayer()
        players.append(newPlayer)
        i = i + 1
    return players
