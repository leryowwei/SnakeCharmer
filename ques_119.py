from ques_base import *

class question_119(question_base):

    def __init__(self):
        self.statement = "Digit power sum"
        self.difficulty = 0.30

    def solve(self):
        # For n = a^b, sum of the digits of n are equal to a.  (b is integer but otherwise not defined)
        # e.g. 512 = 8^3 and 5+2+1=8
        power_sum = []  # Set up list to capture numbers that meet this criteria

        for a in range(1, 1000):
            for b in range(1, 20):
                n = a ** b
                n_str = str(n)  # make n into a string
                n_digits_str = list(n_str)  # make string into a list of letters
                n_digits = list(map(int, n_digits_str))  # make list of letters into a list of ints
                digit_sum = sum(n_digits)
                if digit_sum == a and n > 9:  # if digit sum of n is equal to a, and n has at least two digits
                    power_sum.append(n)
                else:
                    None

        power_sum = sorted(power_sum)  # Sort list in ascending order
        # Take 30th element of list
        return power_sum[30-1]
