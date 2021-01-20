from ques_base import *

class question_120(question_base):

    def __init__(self):
        self.statement = "Square remainders"
        self.difficulty = 0.25

    def solve(self):
        # Looking for max remainder for (a-1)^n + (a+1)^n when divided by a^2
        # (as reminder will vary as you change n. Note that any value of n is permitted)
        # The calculate for sum r_max for 3<=a<=1000

        # The binomial expansion of (1+a)^n is 1 + an + n(n-1)/2! a^2 + n(n-1)(n-2)/3! a^3 ...
        # The binomial expansion of (-1+a)^n is [-1]^n * [1 - an + n(n-1)/2! a^2 - n(n-1)(n-2)/3! a^3 + ...]
        # Thus if n is even => (1+a)^n + (-1+a)^n = 2( 1 + n(n-1)/2! a^2 + n(n-1)(n-2)(n-3)/4! a^4 + ...]
        # and if n is odd => (1+a)^n + (-1+a)^n = 2( an + n(n-1)(n-2)/3! a^3 + n(n-1)(n-2)(n-3)(n-4)/5! a^5 + ...]

        # Now note that if n is even, then every term in a^2 and a^4 and above is exactly a multiple of a^2
        # Therefore, remainder is just 2  => (1+a)^n+(-1+a)^n = 2( 1 + higher order terms that are all multiples of a^2)

        # If n is odd, we re-write (1+a)^n + (-1+a)^n = 2a( n + n(n-1)(n-2)/3! a^2 + n(n-1)(n-2)(n-3)(n-4)/5! a^4 + ...]
        # Therefore, remainder is just 2an  => (1+a)^n+(-1+a)^n = 2a( n + higher terms which are all multiples of a^2)

        # Our problem reduces to finding maximum remainder for any n
        # Maximum possible remainder (by definition) is a^2-1
        # So our problem is reduced to finding the maximum of 2an mod a^2
        # If a is even, then when n=a/2, then remainder is zero, so max remainder is when n = a/2 -1_
        # i.e. if a is even then max remainder = a^2 -2a
        # If a is odd, then when n=(a-1)/2, then 2an=a^2-a, which i going to be the maximum possible
        # i.e. if a is odd then max remainder = a^2 - a

        summation = 0
        for a in range(3, 1001):  # For 3<=a<=1000
            if a % 2 == 0:  # If a is even
                r_max = a ** 2 - 2 * a  # r_max = a^2 - 2a (if a is even)
            else:
                r_max = a ** 2 - a  # r_max = a^2 - a (if a is odd)
            summation += r_max

        return summation
