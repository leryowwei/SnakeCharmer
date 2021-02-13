"""Base class for the questions and also consists of static methods for common/utils functions"""

import math
import time

class question_base:
    statement = None
    difficulty = None
    start_time = None
    end_time = None

    def problem_statement(self):
        return self.statement

    def problem_difficulty(self):
        return self.difficulty

    def difficulty_score(self):
        return self.difficulty ** 1.5

    def start_timer(self):
        self.start_time = time.time()

    def time_spent(self):
        self.end_time = time.time()
        return self.end_time - self.start_time

    # common functions that can be accessed
    @staticmethod
    def smallest_prime_num(n, limit=None):
        """Find out the smallest prime num of a n"""

        if n < 2:
            raise ValueError("Value needs to be >= 2 because the smallest prime number is 2...")

        # if limit not specified by user, set it to n
        if not limit:
            limit = n

        # loop through all values and find out which one has an % == 0
        smallest_prime = None
        for i in range(2, int(limit)):
            if n % i == 0:
                smallest_prime = i
                break

        return smallest_prime

    @staticmethod
    def primes_in_range(lower, upper):
        primes_list=[]
        for num in range(lower, upper + 1):
            # all prime numbers are greater than 1
            if num > 1:
                for i in range(2, int(math.sqrt(num)+1)):  # Only need to check for divisors up to sqrt(n)
                    if (num % i) == 0:
                        break
                else:
                    primes_list.append(num)
        return primes_list
