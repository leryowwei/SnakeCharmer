from ques_base import *


class question_16(question_base):

    def __init__(self):
        self.statement = "Power digit sum"
        self.difficulty = 0.05

    def solve(self):
        n = 2 ** 1000
        str_n = str(n)
        summation = 0
        print(n)
        for i in range(0, len(str_n)):
            summation += int(str_n[i])

        return summation
