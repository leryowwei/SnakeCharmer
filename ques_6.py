from ques_base import *

class question_6(question_base):

    def __init__(self):
        self.statement = "Sum Square Difference"
        self.difficulty = 0.05

    def solve(self):
        """
        Find the difference between the sum of the squares of the first one hundred
        natural numbers and the square of the sum.

        """
        a = 0
        b = 0
        for i in range(1, 101):
            a += i ** 2
            b += i

        b_square = b ** 2
        ans = b_square - a
        return ans
