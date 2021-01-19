class question_base:
    statement = None
    difficulty = None

    def problem_statement(self):
        return self.statement

    def problem_difficulty(self):
        return self.difficulty

    def difficulty_score(self):
        return self.difficulty ** 1.5

    # common functions that can be accessed
    def smallest_prime_num(self, n, limit=None):
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
