import numpy as np
from ques_base import *

class question_62(question_base):
    def __init__(self):
        self.statement = "Cubic Permutation"
        self.difficulty = 0.15

    def solve(self):
        ans = 0

        # initialise a cubic array - ensure no overflow
        arr = np.arange(300, 50000)
        arr = np.power(arr, 3, dtype='int64')
        x_list = []

        # loop through array and for each item, rearrange the digits from small to big
        for i, x in enumerate(arr):
            temp_list = sorted([int(d) for d in str(x)])
            x_list.append("".join(str(d) for d in temp_list))

        # loop through the reformatted list and store the values found in dictionary
        # if the same value/key is in dictionary, increase the value up again
        # end the for loop when 5 is reached
        store_dict = {}
        for x in x_list:
            if x not in store_dict:
                store_dict[x] = 1
            else:
                if store_dict[x] < 5:
                    store_dict[x] += 1

                if store_dict[x] == 5:
                    ans = arr[x_list.index(x)]
                    break

        return ans
