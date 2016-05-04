import random
import math
# Player class represents a player that moves through the game with attributes and behaviors

class Player:

    # Init method serves as a constructor
    # Creates a player with chosen name, base HP of 100, and base attack of 10
    def __init__(self, name, ):
        """

        :rtype : object
        """
        self.name = name
        self.hp = 100
        self.attack = 10
        self.level = 1

    #
    # getName method returns String of Player's name
    # returns: String name
    def getName(self):
        return self.name 


    #
    # getHp method returns int of Player's current HP
    # returns: int hp
    def getHp(self):
        return self.hp
    

    def setHp(self, hp):
        self.hp = hp

    #
    # getAttack method returns int of Player's attack stat
    # returns: int attack
    def getAttack(self):
        return self.attack

    def setAttack(self, attack):
        self.attack = attack

    # param: self
    # getLevel returns int of player's level
    # returns: int level
    def getLevel(self):
        return self.level

    def setLevel(self, level):
        self.level = level

# Monster Superclass: contains all attributes and behaviors for individual monsters
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
    
    def setHp(self, hp):
        self.hp = hp

    def getAttack(self):
        return self.attack

    def question(self):
        pass

#child class of Monster for percentage questions
class PercentMonster(Monster):
    def __init__(self, name):
        Monster.__init__(self, name)
        self.name = PercentMonster

    def getType(self):
        return self.__class__

    # Function to generate a percentage question
    # Returns: the question and answer to the question
    def question(self):
        nums = [10,20,40,80] #creating array of percentges
        num1 = random.choice(nums) #choosing random percentage
        nums2 = [10, 20, 40, 100]
        print
        num2  = random.choice(nums2)
        q1 = "What is " , num1, " percent of ", num2 #question string
        a1 = int((num1/100.0)*num2) #num1 is the percentage, which should mutltiply by num2

        return q1, a1


#Subclass of Monster class for geometry-related monsters

class GeoMonster(Monster):
    def __init__(self, name):
        Monster.__init__(self, name)
        self.name = "GeoMonster"

    def getType(self):
        return(self.__class__)

    def question(self):
        q1 = "What shape has 4 sides?"
        a1 = "square"

        return q1, a1
    
# Subclass of Monster class for geometry-related monsters
class MultiMonster(Monster):
    def __init__(self, name):
        Monster.__init__(self, name)
        self.name = "MultiMonster"
        
    def getType (self):
        return(self.__class__)
    
    def question(self):
        q1 = "What is 90 divded by 10?"
        a1 = 9
        
        return q1, a1
    
#function to decide what monster the player will fight
def decideMonster():
    monsterChoice = (random.randint(0, 2)) #add more numbers for more types of monsters
    #print(monsterChoice)

    if monsterChoice == 0:
        m1 = GeoMonster("Geometry")
        m1.hp = 20
        m1.attack = 2
    elif monsterChoice == 1:
        m1 = PercentMonster("Percentages")
        m1.hp = 20
        m1.attack = 3
        #print(m1.q1)
    elif monsterChoice == 2:
        m1 = MultiMonster("Multiplication")
        m1.hp = 20
        m1.attack = 4

    #Prints the monster's information
    print("Monster's name: {0}".format(m1.getName()))
    print("Monster's HP: {0}".format(m1.getHp()))
    print("Monster's attack stat: {0}".format(m1.getAttack()))

    return m1


#Allows player to answer the question
#Compares the input with the actual answer
#Player attacks if right, monster attacks if wrong
def answerQ(a,q,p):
    pAnswer = (raw_input(q))
    print "DEBUG:", m1.getType()
    if m1.getType() != GeoMonster:
        pAnswer = int(pAnswer)
    print(pAnswer)
    print(a)
    if (pAnswer) == (a):
        print("Congratulations! You got the question right!")
        m1.setHp(m1.getHp() - p.getAttack())
        print("You attacked the monster and its hp is now " , m1.getHp())
    else:
        print("Sorry, you did not get the answer right :(")
        p.setHp(p.getHp() - m1.getAttack())
        print("The monster attacked you and your health is now " , p.hp)


# Creates a player and prints out their initial attributes
name = raw_input("Enter a name for your player: ")
p1 = Player(name)
print("Player's name: {0}".format(p1.getName()))
print("Player's hit point: {0}".format(p1.getHp()))
print("Player's attack points: {0}".format(p1.getAttack()))
print("Player's Level: {0}".format(p1.getLevel()))

m1 = decideMonster()

#main while loop to run program for now with current setup
# while the monster's hp is above zero.
while p1.getHp() > 0 or p1.getLevel() < 4:
    q1,a1 = m1.question()
    answerQ(a1,q1,p1)
    # if the monster is dead, make a new monster
    if m1.getHp() <= 0:
        m1 = decideMonster()
    



