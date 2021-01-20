from ques_base import *

class question_20(question_base):

    def __init__(self):
        self.statement = "Factorial digit sum"
        self.difficulty = 0.05

    def solve(self):
        import math

        hundred_factorial = math.factorial(100)
        str_hundred_factorial = str(hundred_factorial)
        summation = 0
        print(hundred_factorial)
        print(str_hundred_factorial)

        for i in range(0, len(str_hundred_factorial)):
            summation += int(str_hundred_factorial[i])

        return summation
