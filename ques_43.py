from ques_base import *
import itertools

class question_43(question_base):

    def __init__(self):
        self.statement = "Sub-string divisibility"
        self.difficulty = 0.05

    def solve(self):
        # last three digits must be divisible by 17,
        # thus they must either be ...289, or ...867
        digits_a = [0, 1, 3, 4, 5, 6, 7]
        perm_a = list(itertools.permutations(digits_a))  # create permutations for the first 7 digits
        list_a = []
        for l in perm_a:
            n = list(l)
            n.append(2)
            n.append(8)
            n.append(9)  # append digits 289
            list_a.append(n)  # add to list

        digits_b = [0, 1, 2, 3, 4, 5, 9]
        perm_b = list(itertools.permutations(digits_b))
        list_b = []
        for l in perm_b:
            n = list(l)  # create permutations for the first 7 digits
            n.append(8)
            n.append(6)
            n.append(7)
            list_b.append(n)  # add to list

        permutations = list_a + list_b
        # digits = range(0, 10)  # list of numbers 1 to 9
        # permutations = list(itertools.permutations(digits))

        summation = 0
        for n in permutations:
            if (n[7] * 100 + n[8] * 10 + n[9]) % 17 == 0:
                if (n[5] * 100 + n[6] * 10 + n[7]) % 11 == 0 and (n[6] * 100 + n[7] * 10 + n[8]) % 13 == 0:
                    if (n[3] * 100 + n[4] * 10 + n[5]) % 5 == 0 and (n[4] * 100 + n[5] * 10 + n[6]) % 7 == 0:
                        if (n[1] * 100 + n[2] * 10 + n[3]) % 2 == 0 and (n[2] * 100 + n[3] * 10 + n[4]) % 3 == 0:
                            n = int(''.join(map(str, n)))
                            summation += n

        return summation
