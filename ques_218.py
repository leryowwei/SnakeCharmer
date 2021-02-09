from ques_base import *

class question_218(question_base):

    def __init__(self):
        self.statement = "Perfect right-angled triangles"
        self.difficulty = 0.55

    def solve(self):
        # All perfect right angled triangles are also super-perfect right angled triangles
        # Therefore no perfect right angled triangles that are not super pefect exist below 10^16
        answer = 0
        return answer
