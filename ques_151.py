from ques_base import *
from decimal import *


class question_151(question_base):

    def __init__(self):
        self.statement = "Paper sheets of standard sizes: an expected-value problem"
        self.difficulty = 0.50

        # best case solution when there is only one sheet and is A5
        self.d = {(5,): Decimal(0)}

    def calculate(self, pp_size):
        if pp_size in self.d:
            return self.d[pp_size]

        result = Decimal(0)

        if len(pp_size) == 1:
            result += Decimal(1)

        p = Decimal(1) / Decimal(len(pp_size))

        for i in pp_size:
            tmp_curr = list(pp_size)
            tmp_curr.remove(i)
            while (i < 5):
                tmp_curr.append(i + 1)
                i += 1
            tmp_curr = tuple(sorted(tmp_curr))
            result += p * self.calculate(tmp_curr)

        self.d[pp_size] = result

        return result

    def solve(self):
        # start the calculation with A2, A3, A4, A5
        result = self.calculate((2, 3, 4, 5))

        return round(result, 6)



