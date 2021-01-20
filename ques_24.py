from ques_base import *


class question_24(question_base):

    def __init__(self):
        self.statement = "Lexicographic permutations"
        self.difficulty = 0.05

    def solve(self):
        import itertools
        perms = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))  # create list of all possible permutations

        return perms[999999]  # List is already ordered, so one millionth item in list is list[1000000-1]
