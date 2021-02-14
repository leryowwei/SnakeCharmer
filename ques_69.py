from ques_base import *

class question_69(question_base):

    def __init__(self):
        self.statement = "Totient maximum"
        self.difficulty = 0.10

    def solve(self):
        # Totient function, Phi(n) = n*(1-1/p_a)*(1-1/p_b)*...
        # where {p_a, p_b, p_c...} are distinct prime factors of n
        # Maximise n/phi(n) = 1/(1(1-1/p_a)*(1-1/p_b)*...)
        # i.e. minimise (1-1/p_a)*(1-1/p_b)*...
        # Each additional distinct prime factor will reduce the value of this product
        # So choose the number less than 1,000,000, which has the most distinct prime factors
        answer = 2*3*5*7*11*13*17
        return answer
