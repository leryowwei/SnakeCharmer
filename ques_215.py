from ques_base import *

class question_215(question_base):

    def __init__(self):
        self.statement = "Crack-free Walls"
        self.difficulty = 0.50

        # define wall dimensions
        self.wall_width = 32
        self.wall_height = 10
        self.pos_of_crack = []

    def get_crack_positions(self, cracks, position):
        if position < 0:
            raise ValueError()
        elif position < self.wall_width:
            # brick can be width of 2 or 3
            for i in (2, 3):
                cracks.append(position + i)
                self.get_crack_positions(cracks, position + i)
                cracks.pop()
        elif position == self.wall_width:
            self.pos_of_crack.append(frozenset(cracks[: -1]))

    def solve(self):
        # find out all possible position of the bricks for the whole width of wall
        self.get_crack_positions([], 0)

        # find disjoint sets such that the two position of cracks do not intersect
        noncrackindices = [
            [i for (i, cp1) in enumerate(self.pos_of_crack) if cp0.isdisjoint(cp1)]
            for cp0 in self.pos_of_crack]

        ways = [1] * len(self.pos_of_crack)

        # form a list of all possible combinations to get crack free wall throughout the whole height
        for i in range(1, self.wall_height):
            temp_ways = [sum(ways[k] for k in nci) for nci in noncrackindices]
            ways = temp_ways

        return sum(ways)