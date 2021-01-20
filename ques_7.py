from ques_base import *


def prime_number(n):
    "Returns true if number is prime"
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False

    return True


class question_7(question_base):
    def __init__(self):
        self.statement = "10 001st prime number"
        self.difficulty = 0.05

    def solve(self):
        i = 0
        j = 0
        while j < 10001:
            i = i + 1
            if prime_number(i):
                j = j + 1
        ans = i
        return ans
