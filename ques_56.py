from ques_base import *

class question_56(question_base):

    def __init__(self):
        self.statement = "Powerful digit sum"
        self.difficulty = 0.05

    def solve(self):
        max_sum = 0
        for a in range(1, 100):
            for b in range(1, 100):
                n = a ** b
                n_str = str(n)
                n_digits_str = list(n_str)
                n_digits = list(map(int, n_digits_str))
                digit_sum = sum(n_digits)
                if digit_sum > max_sum:
                    max_sum = digit_sum
                else:
                    None

        return max_sum
