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

class Monster:
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.attack = 2
        self.level = 1

    def getName(self):
         return self.name

    def getHp(self):
        return self.hp

    def getAttack(self):
        return self.attack

class FracMonster(Monster):
    def __init__(self, name):
        super().__init__(name)
        self.name = "FracMonster"







p1 = Player("Bob")
print("Player's name: " +p1.getName())
print("Player's hit point: " , p1.getHp())
print("Player's attack points: " , p1.getAttack())
print("Player's Level: " , p1.getLevel())

m1 = FracMonster("Fractions")
m1.hp = 100
m1.attack = 3
print("Monster's name: " + m1.getName())
print("Monster's HP: " , m1.getHp())
print("Monster's attack stat: ", m1.getAttack())