from ques_base import *

class question_63(question_base):

    def __init__(self):
        self.statement = "Powerful digit counts"
        self.difficulty = 0.05

    def solve(self):
        #  a^n = number, if length of this number is equal to n then add 1 to the count
        count = 0
        for a in range(1, 9):  # if a is 10 (or greater) then a^n MUST have more than n digits (e.g. 10^2 = 100)
            for n in range(1, 23):  # 9^22 = 9.847x10^20 which has only 21 digits (i.e. less than n=22)
                if len(str(a**n)) == n:
                    count += 1
        return count
