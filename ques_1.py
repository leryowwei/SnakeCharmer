from ques_base import *

class question_1(question_base):
    def __init__(self):
        self.statement = "Multiples of 3 and 5"
        self.difficulty = 0.05

    def solve(self):
        ans = 0

        for x in range(1, 1000):
            if x % 3 == 0 or x % 5 ==0:
                ans += x
        return ans