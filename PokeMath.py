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
    # returns: String name
    def getName(self):
        return self.name

    #
    # getHp method returns int of Player's current HP
    # returns: int hp
    def getHp(self):
        return self.hp

    #
    # getAttack method returns int of Player's attack stat
    # returns: int attack
    def getAttack(self):
        return self.attack

    # param: self
    # getLevel returns int of player's level
    # returns: int level
    def getLevel(self):
        return self.level

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

    def getAttack(self):
        return self.attack

    def question(self):
        pass

#child class of Monster for percentage questions
class PercentMonster(Monster):
    def __init__(self, name):
        super().__init__(name)
        self.name = "PercentMonster"

    # Function to generate a percentage question
    # Returns: the question and answer to the question
    def question(self):
        nums = [10,20,40,80] #creating array of percentges
        num = random.choice(nums) #choosing random percentage
        nums2 = [10, 20, 40, 100]
        num2  = random.choice(nums2)
        q1 = "What is " , num, " percent of ", num2 #question string
        a1 = int(num2 * (num/100)) #figuring out numerical answer
        #print(a1)

        return q1, a1


#Subclass of Monster class for geometry-related monsters

class GeoMonster(Monster):
    def __init__(self, name):
        super().__init__(name)
        self.name = "GeoMonster"

    def question(self):
        q1 = "What shape has 4 sides?"
        a1 = "square"

#function to decide what monster the player will fight
def decideMonster():
    monsterChoice = (random.randint(0, 1)) #add more numbers for more types of monsters
    #print(monsterChoice)

    if monsterChoice == 0:
        m1 = GeoMonster("Geometry")
        m1.hp = 20
        m1.attack = 2
    elif monsterChoice == 1:
        m1 = PercentMonster("Percentages")
        m1.hp = 100
        m1.attack = 3
        #print(m1.q1)

    #Prints the monster's information
    print("Monster's name: " + m1.getName())
    print("Monster's HP: ", m1.getHp())
    print("Monster's attack stat: ", m1.getAttack())

    return m1


#Allows player to answer the question
#Compares the input with the actual answer
#Player attacks if right, monster attacks if wrong
def answerQ(a,q,p):
    pAnswer = (input(q))
    if m is not GeoMonster:
        pAnswer = int(pAnswer)
    print(pAnswer)
    print(a)
    if (pAnswer) == (a):
        print("Congratulations! You got the question right!")
        m.hp -= p.attack
        print("You attacked the monster and its hp is now " , m.hp)
    else:
        print("Sorry, you did not get the answer right :(")
        p.hp -= m.getAttack()
        print("The monster attacked you and your health is now " , p.hp)


# Creates a player and prints out their initial attributes
name = input("Enter a name for your player: ")
p1 = Player(name)
print("Player's name: " + p1.getName())
print("Player's hit point: ", p1.getHp())
print("Player's attack points: ", p1.getAttack())
print("Player's Level: ", p1.getLevel())

m = decideMonster()

#main while loop to run program for now with current setup
while m.hp > 0:
    q1,a1 = m.question()
    answerQ(a1,q1,p1)


