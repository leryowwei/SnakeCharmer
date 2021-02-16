from ques_base import *

class question_9(question_base):

    def __init__(self):
        self.statement = "ques_8.py"
        self.difficulty = 0.05

    def solve(self):
        """


        """
        for a in range(1,1000):
            for b in range(1,1000):
                c = 1000 - a - b
                if (a ** 2 + b ** 2) == c ** 2:
                    ans = a * b * c
        return ans