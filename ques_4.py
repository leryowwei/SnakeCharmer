import numpy as np
from ques_base import *

class question_4(question_base):
    def __init__(self):
        self.statement = "Largest palindrome product"
        self.difficulty = 0.05

    def solve(self):
        ans = 0

        # initialise numpy arrays and multiply them to get the whole set of products
        x = np.tile(np.arange(100, 1000, 1), 999)
        y = np.repeat(np.arange(100, 1000, 1), 999)
        products = np.multiply(x, y)

        # sort numpy array in ascending order
        products = -np.sort(-products)

        # loop through numpy array and compare the value against its reverse self
        for val in products:
            val = str(val)
            if val == val[::-1]:
                ans = val
                break

        return ans
