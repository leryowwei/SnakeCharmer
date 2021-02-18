from ques_31 import *

class question_76(question_31):

    amount_to_make = 100              # interested in how many ways to make 100
    coins = range(1, amount_to_make)  # can use any number between 1 and 99 (excludes 100)

    def __init__(self):
        self.statement = "Counting summations"
        self.difficulty = 0.1