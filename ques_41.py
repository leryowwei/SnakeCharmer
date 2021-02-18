from ques_base import *
import itertools
import math

class question_41(question_base):

    def __init__(self):
        self.statement = "Pandigital prime"
        self.difficulty = 0.05

    def solve(self):
        # Largest pandigital prime
        # n digits, using the digits 1 to n each once
        # 1+2+3+4+5+6+7+8+9=45 => multiple of 3, thus any 9 digit pandigital number can't be prime
        # But also 1+2+3+4+5+6+7+8 = 36 => multiple of 3, thus any 8 digit pandigital can't be prime
        # Try 8 digit pandigital numbers

        one_to_eight = range(1, 8)  # list of numbers 1 to 7
        permutations = list(itertools.permutations(one_to_eight))
        permutations.reverse()

        primes = primes_in_range(1, 5000)

        for i in permutations:
            n = ''.join(map(str, i))
            n = int(n)
            if is_prime_info(n, primes):
                #print(n)
                break
        return n


def is_prime_info(num, primes_list):
    prime_flag = True
    if num > 1:
        for p in primes_list:  # Only need to check for divisors up to sqrt(n)
            if p*p < num + 1:  # no need to check for divisors greater than the sqrt(num)
                if (num % p) == 0:
                    prime_flag = False
                    break
    else:  # num is not a positive integer, so it cannot be prime
        prime_flag = False
    return prime_flag


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

