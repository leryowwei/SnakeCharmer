from ques_base import *

class question_x(question_base):

    def __init__(self):
        self.statement = "1000-digit Fibonacci number"
        self.difficulty = 0.05

    def solve(self):
        fib = [1, 1]  # Initialise fibonacci sequence list
        while len(str(fib[-1])) < 1000:  # While length of latest fib number is less than 1000 digits
            fib.append(fib[-1] + fib[-2])  # Calculate the next fib number and append it to the list

        return len(fib)
