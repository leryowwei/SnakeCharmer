from ques_base import *


class question_19(question_base):

    def __init__(self):
        self.statement = "Counting Sundays"
        self.difficulty = 0.05

    def solve(self):
        days_of_C20 = [1]  # Initialise a list to show which day of the 20th Century the 1st of each month is
        normal_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # List of month lengths (days) in normal year
        leap_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # List of month lengths (day) in leap year

        for year in range(1901, 2001):  # range doesn't include upper bound, so 1901-2000 is range(1901,2001)
            print(year)
            if year % 400 == 0:  # If year is multiple of 400, then it's a leap year
                for x in range(0, len(leap_months)):
                    days_of_C20.append(days_of_C20[-1] + leap_months[x])
            elif year % 100 == 0:  # If year is a multiple of 100, then it's a normal year
                for x in range(0, len(normal_months)):
                    days_of_C20.append(days_of_C20[-1] + normal_months[x])
            elif year % 4 == 0:  # If year is a multiple of 4, then it's a leap year
                for x in range(0, len(leap_months)):
                    days_of_C20.append(days_of_C20[-1] + leap_months[x])
            else:  # otherwise it's a normal year
                for x in range(0, len(normal_months)):
                    days_of_C20.append(days_of_C20[-1] + normal_months[x])

        del days_of_C20[-1]  # Remove last item in list because this will be the first day of the 21st Century
        print(days_of_C20)
        count_sundays = 0  # Initialise number of sundays which are on 1st day of month
        for i in range(0, len(days_of_C20)):
            if days_of_C20[i] % 7 == 6:  # 6 chosen as 1st Jan 1901 is a Tuesday, so 6th day of 20th Century is a Sunday
                count_sundays += 1

        return count_sundays
