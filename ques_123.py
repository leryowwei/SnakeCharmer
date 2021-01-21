from ques_base import *

class question_123(question_base):

    def __init__(self):
        self.statement = "Prime square remainders"
        self.difficulty = 0.30

    def solve(self):
        # From problem 120 => Remainder of (p-1)^n + (p+1)^n % n, is 2pn. (as primes are always odd)
        # So we can calculate much more simply 2pn % n, to get our remainder
        # (also no need to test any primes where n is even, as this will always give remainder 2)

        #  Calculate a list of primes
        primes = self.primes_in_range(1, 500000)  # Calculate list of primes here
        primes.insert(0, 0)  # Add zero as the first number in the list such that primes[n] is the nth prime

        # Test remainders
        least_n = 0
        for n in range(7037, len(primes)):  # Can start our list at 7037 as per question
            if n % 2 == 0:
                continue
            else:
                r = 2 * n * primes[n] % primes[n] ** 2  # remainder = 2*n*p % p^2
                if r > 10 ** 10:  # If remainder is greater than 10^10
                    least_n = n  # then set least_n as curent value of n and then break out of loop
                    break
        return least_n
