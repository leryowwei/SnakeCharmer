from ques_base import *
import math
class question_174(question_base):

    def __init__(self):
        self.statement = "Counting the number of 'hollow' square laminae that " \
                         "can form one, two, three, ... distinct arrangements"
        self.difficulty = 0.40

    def solve(self):
        # For a given number of tiles 't', there could be a number of ways to make square hole lamina
        # let 'a' be the size of the internal hole, 'b' be the outer edge length and 'w' the width
        # Such that b = a + 2w
        # now t = b^2 - a^2 = ((a+2w)^2 - a^2 = 4w(a+w)
        # a is >= 1
        # so for a given t, the number of ways to make a square hole lamina is equal to
        # the different values of 4w are divisors of t
        # Or more simply, qt = t/4  => qt = w(a+w)
        # So number of different square lamina is equal to the 'small divisors' of qt
        # Where a 'small divisor' is one that is strictly less than sqrt(num)

        t = 1000000  # max number of tiles. qt = t/4
        n_list = [0] * 11  # list to store number of 't's that have exactly 1, 2, 3 ... 9, or 10
        # different ways to make a square hole lamina

        for qt in range(2, t // 4):
            ways = number_of_small_divisors(qt)
            if ways <= 10:
                n_list[ways] += 1

        return sum(n_list)

def number_of_small_divisors(num):
    divisors = 1  # Every number has at least one small divisor - the number "1"
    for d in range(2, int(math.sqrt(num))):  # Start at 2 and go up to just below sqrt(num),
        if num % d == 0:  # if d goes into num exactly, then d is a divisor
            divisors += 1  # so add 1 to the number divisors
    return divisors
