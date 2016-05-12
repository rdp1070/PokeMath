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

    def PercentMonsterLevel2(m1):
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
