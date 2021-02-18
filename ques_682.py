from ques_base import *

class question_682(question_base):

    def __init__(self):
        self.statement = "5-Smooth Pairs"
        self.difficulty = 0.50

    def solve(self):
        ans = five_smooth_equation(10 ** 7)
        return ans

# Alternatively, we can find the different partitions of the set
# { [2,2], [2,3], [2,5], [3,2], [3,3], [3,5], [5,2], [5,3], [5,5] }
# Where the product of the first number in each of the pairs multiplies to p
# And the product of all the second number in each pairs multiplies to q
# being careful to deal with double counting (i.e. ([2,2][3,3]) gives p=6, q=6
# But so does ([2,3][3,2])
# All told the generating function is
# (1 - x + x^4 + x^5 - 2x^6 + x^7 + x^8 - x^11 + x^12)
# ----------------------------------------------------
#        (1-x)(1-x^6)(1-x^7)(1-x^8)(1-x^10)

def five_smooth_sets(num):
    list_abc = []  # list of lists to store sets of (a,b,c) where
    # 'a' is the number of 2's
    # 'b' is the number of 3's
    # 'c' is the number of 5's
    # i.e. 2*a + 3*b + 5*c = num
    if num % 10 == 0:
        n = num // 5  # 'n' 5's sum together to make num
        # Try to make sets of the form (a, b, n-x)
        # The first set will be (0, 0, n)
        for x in range(0, n+1):
            # c = n - x
            for b in range(0, (5*x//3)+1):  # num - 5*(n-x) = leftover = 5*x
                # try fitting some 3's in (between 0 and the maximum of leftover/3)
                if (5*x-3*b) % 2 == 0:  # If 5x - 3b is even, then we can fit some 2's in
                    a = (5*x - 3*b)//2  # This many 2's to be exact (a can be zero)
                    c = n - x
                else:  # If we can't fit any 2's in (not even zero 2's)
                    continue  # Then we don't have a set that sums exactly to num, so try next value for b
                if (a+b+c) % 2 == 0:  # If set has an even number of terms total
                    list_abc.append([a, b, c])  # Add it to our list of lists

    else:
        print("Choose a multiple of 10")

    return list_abc


def pairs_given_abc(abc):
    a = abc[0]
    b = abc[1]
    c = abc[2]
    # For a given combination (a, b, c)
    t = (a + b + c) / 2  # = total terms needed in one half
    if c >= t:  # i.e. if surplus of 5's
        combinations = (a + 1) * (b + 1)
        # we can have any combination of 2's and 3's and the rest fives.
        # e.g. (0,0), (0,1), (0,2) ... (0, b-1), (0, b)
        #      (1,0), (1,1),    ...    (1, b-1), (1, b)
        #      ...
        #      (a-1,0), (a-1, 1)      ...      (a-1, b)
        #      (a,0)  , (a, 1)    ...            (a,b)
    elif b >= t:  # i.e. if surplus of 3's
        combinations = (a + 1) * (c + 1)
    elif a >= t:  # i.e. if surplus of 3's
        combinations = (b + 1) * (c + 1)
    else:  # No clear surplus of any factor
        # we need at least some 2's and 3's to get to exactly t terms, then the rest can be 5's
        # but we can't have all the 2's and all the 3's or we'd have more than t terms
        # So we can't have full size rectangle of combinations,
        # In the upper left we lose a triangle of size ul = t-c = (a+b-c)/2
        # In the bottom right we lose a triangle of size br = a+b-t = (a+b-c)/2
        # So in total we loose ( ul(ul+1)/2 + br(br+1)/2 ) combinations
        # and as ul = br = (a+b-c)/2, the lost combinations are = ul(ul+1)
        ul = (a + b - c) // 2  # Note that (a+b-c) is guaranteed to be even
        combinations = (a + 1) * (b + 1) - ul * (ul + 1)
    return combinations


def five_smooth(number):
    #print("Attempting n = {}".format(number))
    sum = 0
    list_of_abc = five_smooth_sets(number)  # This however is slow
    start_sum=time.time()
    for s in list_of_abc:
       sum += pairs_given_abc(s)  # This is fast
    end_sum=time.time()
    #print("summing took {}s".format(end_sum -start_sum))
    sum %= 1000000007  # give answer as sum = sum % 1000000007, as per problem statement
    return sum


def five_smooth_equation(num):
    #  Computing value for small number of f(10^n) results in the following closed form formula
    # f(10^n) = 10^(4n-1) + 4*10^(3n) + 592*10^(2n-1) + 384*10^n + h(n mod 6) / 4032
    # with h(0) = 4032, h(1) = h(4) = h(5) = 2880 and h(2) = h(3) = 1728

    # num must be of form 10^n
    if int(str(num)[0]) == 1 and int(str(num)[1:]) == 0:
        n = len(str(num)) - 1
        # Let's get the value of n from the length of num
        h = [4032, 2880, 1728, 1728, 2880, 2880]
        five_smooth_numbers = (10**(4*n - 1) + 4*10**(3*n) + 592*10**(2*n - 1) + 384*10**n + h[n % 6])//4032
        #print(five_smooth_numbers)
        answer = five_smooth_numbers % 1000000007
    else:
        print("Not a power of 10")
        answer = 0
    return answer
