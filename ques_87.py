from ques_base import *

class question_87(question_base):

    def __init__(self):
        self.statement = "Prime power triples"
        self.difficulty = 0.20

    def solve(self):
        large = 50000000  # We want to find numbers up to 50 million
        primes = primes_in_range(1, int(math.sqrt(large)))  # List of primes up to sqrt(n)
        primes_c = list_upto(primes, int(large ** (1 / 4)))  # subset of primes up to cube root n
        primes_b = list_upto(primes, int(large ** (1 / 3)))  # subset of primes up to 4th root n
        primes_a = primes
        list_of_n = []  # list to store all numbers made up of a^2 + b^3 + d^4

        for c in primes_c:
            for b in primes_b:
                for a in primes_a:
                    n = a * a + b * b * b + c * c * c * c
                    if n < large:
                        list_of_n.append(n)
                    else:  # if current value of c^4 + b^3 + a^2 is too big,
                        break  # then so will all other 'n' with this combination of c and b and any larger a

        list_of_n.sort()  # Sort list numerically increasing
        new_list = []  # This new list will not contain duplicates

        prev_n = 0
        for n in list_of_n:
            if n != prev_n:
                new_list.append(n)
            prev_n = n

        return len(new_list)

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

def list_upto(long_list, target):
    sublist = long_list
    for p in long_list:
        if p > target:
            i = long_list.index(p)
            sublist = long_list[:i]
            break
    return sublist