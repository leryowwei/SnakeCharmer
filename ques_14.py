from ques_base import *


class question_14(question_base):

    def __init__(self):
        self.statement = "Longest Collatz sequence"
        self.difficulty = 0.05

    def solve(self):
        i_max = 0
        s_max = 0

        for i in range(1, 1000000):  # For each integer 1 to 1000000
            n = i  # Set starting value for sequence
            steps = 0  # Set number of steps to zero
            while n > 1:
                if n % 2 == 0:  # If n is even
                    n /= 2
                    steps += 1
                else:  # If n is odd
                    n = 3 * n + 1
                    steps += 1
                if steps > s_max:  # If number of steps to reach 1 is greater than any previous
                    s_max = steps  # Update the maximum number of steps
                    i_max = i  # Update the starting value which has this number of steps

        return i_max
