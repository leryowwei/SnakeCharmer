from ques_base import *

def compute_hcf(x, y):
    """
    Calculates highest common factor between 2 integers
    """

    # choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


class question_71(question_base):

    def __init__(self):
        self.statement = "Counting Fractions"
        self.difficulty = 0.10

    def solve(self):
        """
        Method:

        2/7 <  n/d < 3/7
        5/14 < n/d < 6/14 and so on...

        find the most elaborate version of 3/7 and reduce until HCF of
        n and d equal 1.
        
        """
        d_limit = 1000000
        n0 = 3
        d0 = 7
        # make multiply n & d uniformly until limit reached
        multiplier = int(d_limit / d0)
        n = n0 * multiplier
        d = d0 * multiplier

        # n needs to be smaller, reducing d will make fraction bigger
        n = n - 1
        flag = True
        while flag:
            d = d - 1 # reduce d until HCF of n and d = 1.
            if compute_hcf(n, d) == 1:
                flag = False
                ans = n

        return n



