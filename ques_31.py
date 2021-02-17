from ques_base import *

class question_31(question_base):

    amount_to_make = 200                     # trying to make £2 i.e. 200 p
    coins = [1, 2, 5, 10, 20, 50, 100, 200]  # the possible coins to use (ordered low to high)
    num_of_comb = [0]*(amount_to_make + 1)   # store previous answers in list (last index should be amount_to_make)
    num_of_comb[0] = 1                       # only one way to make nothing

    def __init__(self):
        self.statement = "Coin sums"
        self.difficulty = 0.05

    def solve(self):
        """loop through all coins that can be used"""
        for i in range(0, len(self.coins)):
            coin_value = self.coins[i]
            """for each amount above the coin value, you can make that amount using the coin and the number of ways you
            can make the previous value.
            
            For example, if the coins is a 10p:
            
            10 pence can be made using a 10p and 0, so 1 way
            11 pence can be made using a 10p and 1, so 1 way
            12 pence can be made using a 10p and 2, so 2 ways (10p + 1p + 1p, 10p + 2p)"""
            for j in range(coin_value, self.amount_to_make + 1):
                prev_amount = j - coin_value
                self.num_of_comb[j] += self.num_of_comb[prev_amount]

        return self.num_of_comb[self.amount_to_make]