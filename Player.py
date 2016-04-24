#Player class represents a player that moves through the game with attributes and behaviors
class Player:
    import math

    #Init method serves as a constructor
    #Creates a player with chosen name, base HP of 100, and base attack of 10
    def __init__(self, name,):

        self.name = name
        self.hp = 100
        self.attack = 10
        self.level = 1;

    #
    # getName method returns String of Player's name
    #
    def getName(self):
        return self.name
    #
    # getHp method returns int of Player's current HP
    #
    def getHp(self):
        return self.hp

    #
    # getAttack method returns int of Player's attack stat
    #
    def getAttack(self):
        return self.attack

    #
    # getLevel returns int of player's level
    #
    def getLevel(self):
        return self.level

#Creates a player and prints out their initial attributes
p1 = Player("Bob")
print("Player's name: " +p1.getName())
print("Player's hit point: " , p1.getHp())
print("Player's attack points: " , p1.getAttack())
print("Player's Level: " , p1.getLevel())

