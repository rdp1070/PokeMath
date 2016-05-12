import random

import pygame
from pygame.locals import *
import Question








"""#sugar Imports
from sugar3.activity.activity import Activity
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ActivityButton


# Gtk Import
from gi.repository import Gtk
from gettext import gettext as _
"""

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
        self.experience = 0

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

    def setExp(self,exp):
        self.experience = exp

    def getExp(self):
        return self.experience

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

    def setAttack(self,att):
        self.attack = att

    def getLevel(self):
        return self.level

    def setLevel(self,level):
        self.level = level

    def question(self):
        pass

#child class of Monster for percentage questions
class PercentMonster(Monster):
    def __init__(self, name):
        Monster.__init__(self, name)
        self.name = "PercentMonster"

    def getType(self):
        return self.__class__

    # Function to generate a percentage question
    # Returns: the question and answer to the question
    def question(self):
        if self.level == 1:
            q1 = Question.PercentMonsterLevel1(self)
            q1, a1, options = q1.makeQ()
            return q1, a1, options


#Subclass of Monster class for geometry-related monsters

class GeoMonster(Monster):
    def __init__(self, name):
        Monster.__init__(self, name)
        self.name = "GeoMonster"

    def getType(self):
        return(self.__class__)

    def question(self):
        q1 = "What shape has 4 sides? "
        a1 = "square"

        options=[]
        return q1, a1,options

    
# Subclass of Monster class for geometry-related monsters
class MultiMonster(Monster):
    def __init__(self, name):
        Monster.__init__(self, name)
        self.name = "MultiMonster"
        
    def getType (self):
        return(self.__class__)
    
    def question(self):
        nums1 = [1,2,3,4,5,6,7,8,9] #creating array of numbers to multiply
        num1 = random.choice(nums1) #choosing random number to multiply
        nums2 = [1,2,3,4,5,6,7,8,9,10]
        num2  = random.choice(nums2)
        q1 = ("What is {0} multiplied by {1}? ").format(num1, num2) #question string
        a1 = int( num1 * num2 ) #What is num1 times num2

        i = 0
        options = []
        while (i<4):
                options.append(random.choice(nums1+nums2));
                i+=1
        return q1, a1,options
    
#function to decide what monster the player will fight
def decideMonster(p1):
    monsterChoice = (random.randint(0, 2)) #add more numbers for more types of monsters
    #print(monsterChoice)

    if monsterChoice == 0:
        m1 = GeoMonster("Geometry")


    elif monsterChoice == 1:
        m1 = PercentMonster("Percentages")

        #print(m1.q1)
    elif monsterChoice == 2:
        m1 = MultiMonster("Multiplication")

    if p1.getLevel() == 1 :
        m1.setLevel(1)
        m1.setHp(10)

    elif p1.getLevel() == 2:
        m1.setLevel(2)
        m1.setHp(20)
        m1.setAttack(2)
    elif p1.getLevel() == 3:
        m1.setLevel(3)
        m1.setHp(30)
        m1.setAttack(3)

    #Prints the monster's information
    print("Monster's name: {0}".format(m1.getName()))
    print("Monster's HP: {0}".format(m1.getHp()))
    print("Monster's attack stat: {0}".format(m1.getAttack()))
    print(("").format())

    return m1


#Allows player to answer the question
#Compares the input with the actual answer
#Player attacks if right, monster attacks if wrong
def answerQ(a,q,p):
    pAnswer = (raw_input(q))
    if m1.getType() != GeoMonster:
        pAnswer = int(pAnswer)
    print("You said {0}".format(pAnswer))
    print("The answer was {0}".format(a))
    if (pAnswer) == (a):
        print("Congratulations! You got the question right!").format()
        m1.setHp(m1.getHp() - p.getAttack())
        print("You attacked the monster and its hp is now {0} ".format(m1.getHp()))
        print(("").format())
    else:
        print("Sorry, you did not get the answer right :(").format()
        p.setHp(p.getHp() - m1.getAttack())
        print("The monster attacked you and your health is now {0}".format(p.hp))
        print(("").format())
    
#do the things to start the game up
def startGame():
    print(" _____      _        __  __       _   _     ")
    print("|  __ \    | |      |  \/  |     | | | |    ")
    print("| |__) |__ | | _____| \  / | __ _| |_| |__  ")
    print("|  ___/ _ \| |/ / _ \ |\/| |/ _` | __| '_ \ ")
    print("| |  | (_) |   <  __/ |  | | (_| | |_| | | |")
    print("|_|   \___/|_|\_\___|_|  |_|\__,_|\__|_| |_|")

startGame()
# Creates a player and prints out their initial attributes
name = raw_input("Enter Your name: ")
p1 = Player(name)
print("Player's name: {0}".format(p1.getName()))
print("Player's hit point: {0}".format(p1.getHp()))
print("Player's attack points: {0}".format(p1.getAttack()))
print("Player's Level: {0}".format(p1.getLevel()))
print(("").format())

m1 = decideMonster(p1)



#main while loop to run program for now with current setup
# while the monster's hp is above zero.

while p1.getHp() > 0 or p1.getLevel() < 4:
    q1,a1,options = m1.question()
    print(options)
    answerQ(a1,q1,p1)
    # if the monster is dead, make a new monster
    if m1.getHp() <= 0:
        print("Woohoo! You killed the monster!")
        oldexp = p1.getExp()
        exp = m1.getLevel()
        p1.setExp(exp + oldexp)
        print("Your experience is now {0}".format(p1.getExp()))
        if (10 <= p1.getExp() < 20):
            p1.setLevel(2)
            print("You leveled up to level 2!")
        if (20 <= p1.getExp() < 30):
            p1.setLevel(3)
            print("You leveled up to level 3!")
        if (30 <= p1.getExp() < 40):
            p1.setLevel(4)
            print("You leveled up to level 2!")
        m1 = decideMonster(p1)


if p1.getHp <= 0:
    print("Sorry, you have met your fatal end to the brutality of mathematics.")

else:
    print("Yay, you have won the game!")