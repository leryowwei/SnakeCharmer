from ques_base import *
import math

class question_173(question_base):

    def __init__(self):
        self.statement = "Using up to one million tiles how many different 'hollow' square laminae can be formed?"
        self.difficulty = 0.30

    def solve(self):
        # How many possible 'square hole lamina' are possible with less than 1000000 tiles?
        # Let outer edge of square be 'b' let inner edge of hole be 'a'
        # t = b^2 -a^2
        # Note that a >= 1
        # and that b >= a + 2
        # and that if a is even, b must be even
        # and if a is odd, b must be odd

        t = 1000000  # Maximum number of tiles
        summation = 0  # Total count of number of possible square hole lamina

        for a in range(1, int(t / 4), 2):  # For odd values of a between 1 and t/4
            b = math.sqrt(t + a * a)  # max value that b can be: b = sqrt(t+a^2)
            b = math.floor(b)  # Round down b to integer
            b = b - (1 - (b % 2))  # if b is even, subtract 1, else keep it as odd
            square_holes = (b - a) // 2  # Number of square hole lamina for a given 'a' with up to 't' tiles
            summation += square_holes

        for a in range(2, int(t / 4), 2):  # For even values of a between 2 and t/4
            b = math.sqrt(t + a * a)  # max value that b can be: b = sqrt(t+a^2)
            b = math.floor(b)  # Round down b to integer
            b = b - (b % 2)  # if b is odd, subtract 1, else keep it as even
            square_holes = (b - a) // 2  # Number of square hole lamina for a given 'a' with up to 't' tiles
            summation += square_holes

        return summation
