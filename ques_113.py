from ques_base import *
import operator as op
from functools import reduce

class question_113(question_base):

    def __init__(self):
        self.statement = "Non-bouncy numbers"
        self.difficulty = 0.30

    def solve(self):
        # Decreasing numbers:
        # take a number of n digits, with d allowable digits
        # To be a decreasing number, we can imagine assigning a counter between each digit
        # when we hit a counter we decrement the digit used in the next location by 1 per counter
        # we need (d-1) counters
        # for an n digit number there (n+1) spaces just before/after where we could put counters
        # e.g. for n=5, and d = 4 (hence using digits 9, 8, 7 and 6)
        # []'[][][]''[] = > 98886
        # This problem is akin to placing c=(d-1) identical counters into b=(n+1) bins.
        # The number of ways to do this is (c+h-1)!/(c! * (h-1)!) = ((d-1)+n)!/((d-1)!*n!) = (n+d-1)C(d-1) = (n+d-1)Cn
        # Given that we're using 10 digit [0,1,2,3,4,5,6,7,8,9], d=10, d-1 = 9
        # So there are (n+9)C9 possible n digit decreasing numbers
        # However note that this includes "flat" numbers, such as 4444444 and 3333333 and even 0000000
        # So to get strictly decreasing numbers of length n => (n+9)C9 - 10

        # Increasing numbers:
        # The same logic can be used in again, but this time counters increment the digit.
        # However, this time, in order to get numbers that are of exactly length 'n'
        # we don't want to include 0 in our list of possible digits,
        # as 000127 is not 'really' a 6 digit number, but rather a 3 digit number
        # i.e. d=9 [1,2,3,4,5,6,7,8,9], and thus (d-1) = 8
        # However, if we do want all decreasing number from length 0 to length n we could include the digit zero
        # Again this is also going to catch the "flat" numbers 333333, 444444 etc
        # So to get strictly decreasing numbers of length n => (n+8)C8 - 10

        # It seems like you should be able to flip an increasing number and get a decreasing number.
        # However this isn't quite true. As there are some decreasing number that we cant get to
        # e.g. if we find all increasing numbers up to n digits using (n+9)C9, we can get numbers such as 00127
        # but we can't get the decreasing number 721, as trying to flip gets us 72100

        # Bouncy numbers
        # Bouncy numbers are all numbers that are neither strictly decreasing, nor strictly increasing, nor flat
        # i.e. Consider all the 5 digits numbers (10000 - 99999) n = 5
        # the total number of numbers with 5 digits is 90000 = 9*10^4 = 9 * 10^(n-1)
        # the total number of bouncy numbers with 5 digits is 90000 - ((5+9)C9 - 10) - ((5+8)C8 - 10)
        # = 90000 - 14C9 - 13C8 + 10
        # total number of n digit numbers - decreasing numbers - increasing numbers + double counted flat numbers

        # All 99 numbers between 1-99 are Non-bouncy
        non_bouncy = 99

        for n in range(3, 100 + 1):  # For all numbers between 100 and 999,999 (i.e. 3 digit to 6 digit)
            all_ndigit_numbers = 9 * (10 ** n)
            # print(all_ndigit_numbers)
            decreasing = combinations(n + 9, 9)
            increasing = combinations(n + 8, 8)
            # print(increasing)
            # print(decreasing)
            flat = 10
            non_bouncy += decreasing + increasing - flat
        return non_bouncy


def combinations(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom
