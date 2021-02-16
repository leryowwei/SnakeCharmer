from ques_base import *

class question_235(question_base):

    def __init__(self):
        self.statement = "An Arithmetic Geometric Sequence"
        self.difficulty = 0.40

    @staticmethod
    def func_u(k, r):
        return (900 - 3 * k) * pow(r, k - 1)

    def solve(self):

        # define constants
        lo = 1.001
        hi = 1.003
        eps = 1e-13
        tot = -600000000000

        while hi - lo > eps:
            r = (hi + lo) * 0.5

            s = 0
            # calculate sum from 1 to 5000 using function U
            for i in range(1, 5001):
                s += self.func_u(i, r)

            if s < tot:
                hi = r
            else:
                lo = r

        # return with 12 dp
        return "%.12f" % r
