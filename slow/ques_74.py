from ques_base import *
import math

class question_74(question_base):

    maximum = 1000000
    longest_chain = 60

    len_of_chain = [0] * maximum

    len_of_chain[1] = 1
    len_of_chain[2] = 1

    len_of_chain[145] = 1

    len_of_chain[169] = 3
    len_of_chain[363601] = 3
    len_of_chain[1454] = 3

    len_of_chain[871] = 2
    len_of_chain[45361] = 2

    len_of_chain[872] = 2
    len_of_chain[45362] = 2

    len_of_chain[40585] = 1

    def __init__(self):
        self.statement = "Digit factorial chains"
        self.difficulty = 0.15

    def solve(self):
        ans = 0

        for i in range(1, self.maximum):
            if self.len_of_chain[i] == 0:
                chain = self.calculate_chain(i)
                idx = len(chain) - 1
                length = self.len_of_chain[chain[idx]]
                for idx in range(len(chain)-2, -1, -1):
                    length += 1
                    if chain[idx] <= self.maximum:
                        self.len_of_chain[chain[idx]] = length
                #print("For "+str(i)+", the length of the chain is "+str(self.len_of_chain[i]))
                if self.len_of_chain[i] == 60:
                    ans += 1

        return ans

    def calculate_fact_of_digits(self, num, max_i=6):
        digits = []
        for i in range(0,max_i+1):
            # which digit i.e. 1s, 10s, 100s
            unit = 10**i

            # break if no relavent digit (e.g. 100s of num = 13)
            if num < unit:
                break

            digit = num % (unit*10)         # remove left digits
            digit = math.floor(digit/unit)  # remove right digits
            digits.append(digit)

        sum = 0
        for n in digits:
            sum += math.factorial(n)

        return sum

    def calculate_chain(self, num):
        chain = [num]
        for count in range(0, self.longest_chain):
            next = self.calculate_fact_of_digits(chain[count])
            if next == chain[count]:
                self.len_of_chain[next] = 1
                print(chain)
                return chain
            chain.append(next)
            if next <= self.maximum:
                if self.len_of_chain[next] != 0:
                    return chain