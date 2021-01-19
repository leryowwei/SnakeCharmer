from ques_base import *

class question_3(question_base):
    def __init__(self):
        self.statement = "Largest prime factor"
        self.difficulty = 0.05

    def solve(self):
        ans = 0
        value_given = 600851475143

        # start to solve
        current_value = value_given

        smallest_num = True

        while smallest_num:
            # find out smallest number
            # since current_value = smallest prime factor * larger prime factor, we can assume that the larger prime factor
            smallest_num = self.smallest_prime_num(current_value)

            # if smallest number exists, divide current value
            if smallest_num:
                current_value = current_value / smallest_num
            else:
                ans = current_value

        return ans

