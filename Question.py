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
        q1 = ("What is {0} percent of {1} ").format(num1, num2)  # question string
        a1 = int((num1 / 100.0) * num2)  # num1 is the percentage, which should mutltiply by num2
        i = 0
        options = []
        while (i<4):
            options.append(random.choice(nums+nums2))
            i+=1
        return q1, a1, options

    def makeQ2(self):
        nums = [10, 20, 40, 80]  # creating array of percentges
        num1 = random.choice(nums)  # choosing random percentage
        nums2 = [10, 20, 40, 100]
        print
        num2 = random.choice(nums2)
        q1 = ("What is {0} percent of {1} ").format(num1, num2)  # question string
        a1 = int((num1 / 100.0) * num2)  # num1 is the percentage, which should mutltiply by num2

        i = 0
        options = []
        while (i<4):
                options.append(random.choice(nums+nums2))
                i+=1
        return q1, a1, options
    
#Subclass of Monster class for geometry-related monsters
class GeoMonsterLevel1(Question):
    def __init__(self, monster):
        Question.__init__(self, monster)
        self.name = "GeoMonsterLevel1"

    def getType(self):
        return(self.__class__)

    def makeQ(self):
        q1 = "What shape has 4 equal sides? "
        a1 = "square"

        options=[]
        return q1, a1, options
    
    def makeQ2(self):
        nums = [10, 20, 40, 80]  # creating array of percentges
        num1 = random.choice(nums)  # choosing random percentage
        nums2 = [10, 20, 40, 100]
        print
        num2 = random.choice(nums2)
        q1 = ("What is {0} percent of {1} ").format(num1, num2)  # question string
        a1 = int((num1 / 100.0) * num2)  # num1 is the percentage, which should mutltiply by num2

        i = 0
        options = []
        while (i<4):
            options.append(random.choice(nums+nums2))
            i+=1
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
            options.append(random.choice(nums1+nums2));
            i+=1
        return q1, a1, options
    
     
    def makeQ2(self):
        nums1 = [2,3,4,5,6,7,8,9,10] #creating array of numbers to multiply
        num1 = random.choice(nums1) #choosing random number to multiply
        nums2 = [2,3,4,5,6,7,8,9,10]
        num2  = random.choice(nums2)
        q1 = ("What is {0} multiplied by {1}? ").format(num1, num2) #question string
        a1 = int( num1 * num2 ) #What is num1 times num2

        i = 0
        options = []
        while (i<4):
            options.append(random.choice(nums1+nums2));
            i+=1
        return q1, a1, options