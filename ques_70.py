from ques_base import *
import math

class question_70(question_base):

    def __init__(self):
        self.statement = "Totient permutation"
        self.difficulty = 0.20

    def solve(self):
        large = 10000000  # Up to 10^7
        min_n_phi = 2  # min value of n/phi(n) will eventually be just larger than 1, so set initial value to 2
        # To get min value of n/phi(n), ideally we'd want a prime
        #  However, phi(prime) = prime - 1, so can't be a permutation
        #  The next best thin is a semi-prime, a number with just two prime factors
        #  Ideally, these would be prime factors that are almost equal in magnitude
        #  So construct and test likely semi-primes by multiplying two primes that are ~sqrt(large)
        # I'm going to choose primes between 2000 and 5000 (as 2000*5000=10,000,000)
        primes = primes_in_range(2000, 5000)  # Calculate primes

        for a in primes:
            for b in primes:
                n = a * b
                if n > large:  # if a*b is greater than large
                    break  # break the loop and try the next value of 'a'
                elif a == b:
                    phi_n = int(n * (1 - (1 / a)))  # if one unique prime factor, phi(n) = n(1-1/p)
                else:
                    phi_n = int(n * (1 - (1 / a)) * (1 - (1 / b)))  # calculation of phi(n) for two distinct factors
                if n / phi_n < min_n_phi and is_perumutation(n, phi_n):
                    # if phi(n) is a permutation of n and new lowest value of n/phi(n)
                    min_n_phi = n / phi_n
                    answer = n
        return answer

def is_perumutation(n1, n2):
    str1 = str(n1)  # Convert numbers to strings
    str2 = str(n2)
    if len(str1) == len(str2):  # If equal length strings
        count1 = [0] * 10  # List of how many times each digit appears
        count2 = [0] * 10
        for i in str1:  # for each digit in the string
            count1[int(i)] += 1  # add one to the count of how many times this digit appears
        for i in str2:
            count2[int(i)] += 1
        if count1 == count2:
            is_perm = True
        else:
            is_perm = False
    else:  # Can't be a permutation as different length
        is_perm = False

    return is_perm

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
