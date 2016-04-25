import random
# Player class represents a player that moves through the game with attributes and behaviors

class Player:

    # Init method serves as a constructor
    # Creates a player with chosen name, base HP of 100, and base attack of 10
    def __init__(self, name, ):
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


# Creates a player and prints out their initial attributes

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


class PercentMonster(Monster):
    def __init__(self, name):
        super().__init__(name)
        self.name = "PercentMonster"
    nums = [10,20,40,80]
    num = random.choice(nums)
    nums2 = [10, 20, 40, 100]
    num2  = random.choice(nums2)
    q1 = "What is " , num, " percent of ", num2
    a1 = int(num2 * (num/100))
    print(a1)


class GeoMonster(Monster):
    def __init__(self, name):
        """

        :rtype : Monster
        """
        super().__init__(name)
        self.name = "GeoMonster"
    q1 = "What shape has 4 sides?"
    a1 = "square"


def decideMonster():
    monsterChoice = (random.randint(0, 1))
    print(monsterChoice)

    if monsterChoice == 0:
        m1 = GeoMonster("Geometry")
        m1.hp = 20
        m1.attack = 2
    elif monsterChoice == 1:
        m1 = PercentMonster("Percentages")
        m1.hp = 100
        m1.attack = 3
        #print(m1.q1)



    print("Monster's name: " + m1.getName())
    print("Monster's HP: ", m1.getHp())
    print("Monster's attack stat: ", m1.getAttack())

    return m1

def answerQ(m):
    pAnswer = input(m.q1)
    print(pAnswer)
    print(m.a1)
    if pAnswer.__eq__(m.a1):
        print("Congratulations! You got the question right!")
        m.hp -= 1
        print("You attacked the monster and its hp is now " , m.hp)


name = input("Enter a name for your player: ")
p1 = Player(name)
print("Player's name: " + p1.getName())
print("Player's hit point: ", p1.getHp())
print("Player's attack points: ", p1.getAttack())
print("Player's Level: ", p1.getLevel())

m = decideMonster()
answerQ(m)

