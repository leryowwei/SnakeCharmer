from ques_base import *

class question_86(question_base):

    def __init__(self):
        self.statement = "Cuboid route"
        self.difficulty = 0.35

    def solve(self):
        import math

        # For a cuboid with a>b>c
        # The shortest route between opposite verifies is
        # sqrt(a^2 + (b+c)^
        # Let bc = b + c

        large = 1000000
        count = 0
        a = 0
        while count < large:
            a += 1
            for bc in range(3, 2 * a + 1):
                d = math.sqrt(a * a + bc * bc)  # distance of shortest route
                if d == int(d):  # If d is an integer
                    # print("a is {}, bc is {}, d is {}".format(a, bc, d))
                    if bc <= a:  # if b+c is less than a, then all possible value where b>=c are possible
                        # print("add {} to count".format(bc//2))
                        count += bc // 2  # i.e. floor(bc/2)
                    else:  # bc > a, so possible values of b are 'a' minus when b<c
                        # print("add {} to count".format(a - ((bc-1)//2)))
                        count += 1 + a - ((bc + 1) // 2)
        return a
