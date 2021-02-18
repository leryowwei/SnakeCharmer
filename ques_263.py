from ques_base import *
import math


class question_263(question_base):

    def __init__(self):
        self.statement = "An engineers' dream come true"
        self.difficulty = 0.75

    def solve(self):
        Answer = verify_engineers_paradise()
        return Answer


def is_practical(num, primes):
    if num % 2 == 0:  # If num is even then it could be practical
        practical_flag = True  # Tentatively set practical flag to True
        factors = prime_factorisation(num, primes)  # Find prime factors of num and add to a list
        for i in range(1, len(factors)):  # upper limit is len(factors) rather than len(factors+1)
            # as we don't want to consider the complete list, only subset of the list
            subset = factors[:i]  # Take a sub sequence of the first 'i' prime factors
            product = prod(subset)  # Take product of the subset of prime factors
            sum_of_divisors = divisor_sum(product)  # Find the sum of the divisors of product
            if sum_of_divisors + 1 < factors[i]:  # if the factors of the product of the subsequence are
                # less than the next largest prime factor, then we wont be able to sum the divisors of num to make
                # that next largest prime factor - 1.
                practical_flag = False  # So set practical flag to false
    else:  # If num is odd then it can't be practical
        practical_flag = False

    return practical_flag


def is_prime(num, primes_list):
    if num % 1 == 0 and num > 0 and num < primes_list[-1] ** 2:
        # If num is a positive integer then is see if it's prime
        prime_flag = True
        if num > 1:
            for p in primes_list:  # Only need to check for divisors up to sqrt(n)
                if p ** 2 < num:  # no need to check for divisors greater than the sqrt(num)
                    if (num % p) == 0:
                        prime_flag = False
                        break
                    else:  # num must be prime as it has no exact factors which are less than its sqrt
                        None
                else:  # no need to check for divisors greater than the sqrt(num)
                    None
    else:  # num is not a positive integer, so it cannot be prime
        prime_flag = False
    return prime_flag


def divisor_sum(num):
    if num % 1 == 0 and num > 0:  # If num is a positive integer then calculate and sum its divisors
        divisors = [1, num]  # Set up list with 1 and num (as these will always be divisors)
        for d in range(2, int(math.sqrt(num) + 1)):  # Start at 2 and go up to the sqrt(num),
            # As any larger divisors will be of the form 'num/d'
            if num % d == 0:  # if d goes into num exactly, then d is a divisor
                divisors.append(d)  # so append d to the list of divisors
                if d ** 2 != num:  # if d^2 = number, then num/d = d, so we don't want to add it twice
                    divisors.append(num // d)  # if not, then add num/d to our list as num/d is also a divisor
                else:
                    continue
            else:
                continue
        divisor_summation = sum(divisors)
    else:  # num is not a positive integer, so return zero
        divisor_summation = 0
    return divisor_summation


def prime_factorisation(num, primes_list):
    factors = []
    if num > 0:  # If num is positive integer then calculate its prime factors
        n = num  # We will use n as our test value (which will change as we find our prime factors)
        i = 0
        p = primes_list[i]  # Initial value to test is 2, as it is the first prime
        while p * p < n + 1:  # Start at 2 and go up to sqrt(n)
            # as prime factors will always be less than sqrt(n)
            if n % p == 0:  # If i goes into n exactly, then i is a factor
                factors.append(p)
                n //= p  # n = n/i, divide the number that we are testing so that we don't find the same factor again
            else:  # increase the number we are dividing by
                i += 1
                p = primes_list[i]  # ideally to the next prime number, but in lue of that try the next odd number

        # eventually we have an 'n' which doesn't have any prime factors itself
        factors.append(n)  # so add this to the list of prime factors

    else:  # if num is not a positive integer, then return an empty list
        factors = []
    return factors


def prod(list):
    product = 1
    for i in list:
        product *= i
    return product


def gen_primes():
    # Sieve of Eratosthenes
    D = {}
    x = 2

    while True:
        if x not in D:
            yield x
            D[x * x] = [x]
        else:
            for p in D[x]:
                D.setdefault(p + x, []).append(p)
            del D[x]

        x += 1


def run_gen_primes(num):
    known_primes = [2]  # Start list of primes with the first prime, 2
    prime_generator = gen_primes()
    while num > known_primes[-1]:
        known_primes.append(next(prime_generator))
    return known_primes


def sexy(a, b):
    return b - a == 6


def gen_triple_pair_n():
    prime_generator = gen_primes()
    (i, j, k, l) = (next(prime_generator), next(prime_generator), next(prime_generator), next(prime_generator))
    while True:
        if not sexy(k, l):
            (i, j, k, l) = (l, next(prime_generator), next(prime_generator), next(prime_generator))
            continue

        if (not sexy(j, k)):
            (i, j, k, l) = (k, l, next(prime_generator), next(prime_generator))
            continue

        if (sexy(i, j)):
            yield (i + 9)

        (i, j, k, l) = (j, k, l, next(prime_generator))


def find_engineers_paradise():
    engineers_paradise = []  # Set up an empty list to contain engineers' paradise numbers
    gen = gen_triple_pair_n()  # Define a generator function for triple pairs
    p = run_gen_primes(100000)  # Find primes up to 100000, will allow prime factorisation up to 10 billion
    while len(engineers_paradise) < 4:
        n = next(gen)  # Generate the center point of the next triple pair
        if is_practical(n - 8, p) and is_practical(n - 4, p) and is_practical(n, p) and is_practical(n + 4, p) \
                and is_practical(n + 8, p):
            engineers_paradise.append(n)  # Add n to paradise list
    #print("Engineers' paradises are {}".format(engineers_paradise))
    return sum(engineers_paradise)


def verify_engineers_paradise():
    engineers_paradise = []  # Set up an empty list to contain engineers' paradise numbers
    p = run_gen_primes(100000)  # Find primes up to 100000, will allow prime factorisation up to 10 billion
    for n in [219869980, 312501820, 360613700, 1146521020]:
        if is_prime(n - 9, p) and is_prime(n - 3, p) and is_prime(n + 3, p) and is_prime(n + 9, p):
            if is_practical(n - 8, p) and is_practical(n - 4, p) and is_practical(n, p) \
                    and is_practical(n + 4, p) and is_practical(n + 8, p):
                if not is_prime(n - 7, p) and not is_prime(n - 5, p) and not is_prime(n - 1, p) \
                        and not is_prime(n + 1, p) and not is_prime(n + 5, p) and not is_prime(n + 7, p):
                    engineers_paradise.append(n)  # Add n to paradise list
    #print("Engineers' paradises are {}".format(engineers_paradise))
    return sum(engineers_paradise)
