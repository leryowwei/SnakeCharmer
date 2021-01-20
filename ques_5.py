import numpy as np
from ques_base import *

class question_5(question_base):
    def __init__(self):
        self.statement = "Smallest Multiple"
        self.difficulty = 0.05

    def solve(self):
        ans = 1
        factors = []

        # initiate numpy array with factors
        num_range = np.arange(1, 21)

        # hardcode prime numbers for values below 20
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]

        # loop through prime numbers and check how many times maximum the prime number can divide any number in the list
        # of numbers from 1 to 20
        # e.g. 2 is divisible four times maximum... 2 is divisible by 2 (2^1), 4 (2^2)... 16 (2^4), 18(2 x 3^2), 20 (2^2 x 5)
        for p in prime_numbers:
            counter = 0
            temp_nums = num_range
            while any(temp_nums % p == 0):
                temp_nums = temp_nums / float(p)
                counter += 1
            factors.append(counter)

        # convert list to np array
        factors = np.array(factors)

        # final answer = 2 ^ n * 3 ^ n .... * 19 ^ n where n is the max number found above
        for m in prime_numbers ** factors:
            ans = m * ans

        return ans
