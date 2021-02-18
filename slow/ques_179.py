from ques_base import *

class question_179(question_base):

    def __init__(self):
        self.statement = "Consecuative positive divisors"
        self.difficulty = 0.25

    def solve(self):

        size = 10000000

        list_of_divisors = [1] * (size + 1)  # a list where list[i] = number of divisors of i

        for i in range(2, size + 1):  # iterate through the list
            for j in range(i, size + 1, i):  # for every j'th term add 1
                list_of_divisors[j] += 1  # i.e. every 2nd term is divisible by 2,
                                        # every third term is divisible by 3 etc

        consecutive = 0
        for i in range(1, size):  # if consecutive values of i have the same number of divisors
            if list_of_divisors[i] == list_of_divisors[i + 1]:
                consecutive += 1  # add one to our count

        return consecutive
