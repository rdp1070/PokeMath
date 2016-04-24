#Player class represents a player that moves through the game with attributes and behaviors
class Player:
    import math

    #Init method serves as a constructor
    #Creates a player with chosen name, base HP of 100, and base attack of 10

    def __init__(self, name,):
        self.name = name
        self.hp = 100
        self.attack = 10
