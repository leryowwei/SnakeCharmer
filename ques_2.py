from ques_base import *

class question_2(question_base):
    maximum = 4000000

    def __init__(self):
        self.statement = "Even Fibonacci numbers"
        self.difficulty = 0.05

    def solve(self):
        ans = 0

        prev = [1, 2]
        for num in prev:
            if num % 2 == 0:
                ans += num

        next_num = prev[0] + prev[1]
        while next_num <= self.maximum:
            if next_num % 2 == 0:
                ans += next_num
            prev[0] = prev[1]
            prev[1] = next_num
            next_num = prev[0] + prev[1]

        return ans