from ques_base import *


class question_14(question_base):

    big_number = 100000
    num_of_factors = 500

    def __init__(self):
        self.statement = "Highly divisible triangular number"
        self.difficulty = 0.05

    def solve(self):
        last_tri_num = 0

        for i in range(1, self.big_number):
            last_tri_num += i
            fact = self.get_all_factors(last_tri_num)
            if len(fact) > self.num_of_factors:
                return last_tri_num