"""
Class: Player

Description: Our class player.

"""
class Player:
    def __init__(self, id, name, weight, experience):
        """ constructor
        Setup our player.
        :parameter id           The player id
        :parameter name         The player name
        :parameter weight       The player weight in kg (float)
        :parameter experience   The player experience in years (int)
        """
        self.id = id
        self.name = name
        self.weight = weight
        self.experience = experience
