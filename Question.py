__author__ = 'Mars'
import random


class Question:
    def __init__(self, monster):
        self.name = "Question"
        self.monster = monster


class PercentMonsterLevel1(Question):
    def __init__(self, monster):
        Question.__init__(self,monster)
        self.name = "PercentMonsterLevel1"

    def makeQ(self):
        nums = [10, 50]  # creating array of percentges
        num1 = random.choice(nums)  # choosing random percentage
        nums2 = [10, 20, 40, 100]
        print
        num2 = random.choice(nums2)
        q1 = ("What is {0} percent of {1}?").format(num1, num2)  # question string
        i = 0
        options = []
        while (i<4):
            options.append(random.randint(0,100))
            i+=1


        a1 = int((num1 / 100.0) * num2)  # num1 is the percentage, which should mutltiply by num2
        options.append(a1)
        random.shuffle(options)
        print("Choose the correct answer: {0}").format(options)
        return q1, a1, options


class PercentMonsterLevel2(Question):
    def __init__(self,monster):
        Question.__init__(self,monster)
        self.name = "PercentMonsterLevel2"

    def makeQ(self):
        nums = [10, 20, 40, 80]  # creating array of percentges
        num1 = random.choice(nums)  # choosing random percentage
        nums2 = [10, 20, 40, 100]
        print
        num2 = random.choice(nums2)
        q1 = ("What is {0} percent of {1} ").format(num1, num2)  # question string

        i = 0
        options = []
        while (i<4):
                options.append(random.randint(0,100))
                i+=1

        a1 = int((num1 / 100.0) * num2)  # num1 is the percentage, which should mutltiply by num2

        options.append(a1)
        random.shuffle(options)
        print("Choose the correct answer: {0}").format(options)
        return q1, a1, options

#Subclass of Monster class for geometry-related monsters
class GeoMonsterLevel1(Question):
    def __init__(self, monster):
        Question.__init__(self, monster)
        self.name = "GeoMonsterLevel1"

    def getType(self):
        return(self.__class__)

    def makeQ(self):
        shapes = ["Square", "Rectangle", "Triangle", "Octagon", "Pentagon", ]
        shape = random.sample(shapes, 1)[0]
        q1 = ("How many sides does a {0} have?").format(shape)

        options = [3,4,8,5]



        if shape == "Square" or shape =="Rectangle":
            a1 = 4
        elif shape == "Triangle":
            a1 = 3
        elif shape == "Octagon":
            a1=8
        elif shape =="Pentagon":
            a1=5
        print("Choose the correct answer: {0}").format(options)
        return q1, a1, options

class GeoMonsterLevel2(Question):
    def __init__(self, monster):
        Question.__init__(self, monster)
        self.name = "GeoMonsterLevel2"

    def getType(self):
        return(self.__class__)

    def makeQ(self):
        angle = random.randint(0,180)
        q1 = ("What kind of angle is a {0} degrees?").format(angle)
        options = ["Acute" , "Right" , "Obtuse"]
        if (angle < 90):
            a1 = "acute"
        elif angle == 90:
            a1 = "right"
        elif angle > 90:
            a1 = "obtuse"
        print("Choose the correct answer: {0}").format(options)
        return q1,a1,options

class GeoMonsterLevel3(Question):
    def makeQ(self):
        angles = [30, 45, 60, 90, 120, 180]
        angle = random.choice(angles)
        q1 = ("How many {0} degree angles are needed to make a full circle?").format(angle)
        a1 = 360 / angle
        options = [12, 8, 6, 4, 3, 2]
        random.shuffle(options)
        print("Choose the correct answer: {0}").format(options)
        return q1, a1, options

# Subclass of Monster class for geometry-related monsters
class MultiMonsterLevel1(Question):
    def __init__(self, monster):
        Question.__init__(self, monster)
        self.name = "MultiMonsterLevel1"

    def makeQ(self):
        nums1 = [1,2,5,10] #creating array of numbers to multiply
        num1 = random.choice(nums1) #choosing random number to multiply
        nums2 = [1,2,3,4,5,6,7,8,9,10]
        num2  = random.choice(nums2)
        q1 = ("What is {0} multiplied by {1}? ").format(num1, num2) #question string
        a1 = int( num1 * num2 ) #What is num1 times num2

        i = 0
        options = []
        while (i<4):
            options.append(random.randint(1, 100))
            i+=1
        options.append(a1)
        random.shuffle(options)
        print("Choose the correct answer: {0}").format(options)
        return q1, a1, options


class MultiMonsterLevel2(Question):
    def makeQ(self):
        nums1 = [2,3,4,5,6,7,8,9,10] #creating array of numbers to multiply
        num1 = random.choice(nums1) #choosing random number to multiply
        nums2 = [2,3,4,5,6,7,8,9,10]
        num2  = random.choice(nums2)
        q1 = ("What is {0} multiplied by {1}? ").format(num1, num2) #question string
        a1 = int( num1 * num2 ) #What is num1 times num2

        i = 0
        options = []
        while (i<4):
            options.append(random.randint(1,100))
            i+=1
        options.append(a1)
        random.shuffle(options)
        print("Choose the correct answer: {0}").format(options)
        return q1, a1, options
class MultiMonsterLevel3(Question):
    def makeQ(self):
        nums1 = [6,7,8,9,10] #creating array of numbers to multiply
        num1 = random.choice(nums1) #choosing random number to multiply
        nums2 = [10,11,12,20,25,50]
        num2  = random.choice(nums2)
        q1 = ("What is {0} multiplied by {1}? ").format(num1, num2) #question string
        a1 = int( num1 * num2 ) #What is num1 times num2

        i = 0
        options = []
        while (i<4):
            options.append(random.randint(1,100))
            i+=1
        options.append(a1)
        random.shuffle(options)
        print("Choose the correct answer: {0}").format(options)
        return q1, a1, options