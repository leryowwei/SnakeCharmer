from ques_base import *


class question_17(question_base):

    def __init__(self):
        self.statement = "Number letter counts"
        self.difficulty = 0.05

    def solve(self):
        one_to_nine = (len("one") + len("two") + len("three") + len("four") + len("five") +
                       len("six") + len("seven") + len("eight") + len("nine"))

        ten_to_nineteen = (
                    len("ten") + len("eleven") + len("twelve") + len("thirteen") + len("fourteen") + len("fifteen") +
                    len("sixteen") + len("seventeen") + len("eighteen") + len("nineteen"))

        twenties = (len("twenty") * 10 + one_to_nine)
        thirties = (len("thirty") * 10 + one_to_nine)
        fourties = (len("forty") * 10 + one_to_nine)
        fifties = (len("fifty") * 10 + one_to_nine)
        sixties = (len("sixty") * 10 + one_to_nine)
        seventies = (len("seventy") * 10 + one_to_nine)
        eighties = (len("eighty") * 10 + one_to_nine)
        nineties = (len("ninety") * 10 + one_to_nine)

        one_to_ninetynine = (one_to_nine + ten_to_nineteen + twenties + thirties + fourties + fifties + sixties
                             + seventies + eighties + nineties)

        one_hundreds = (len("onehundred") + len("onehundredand") * 99 + one_to_ninetynine)
        two_hundreds = (len("twohundred") + len("twohundredand") * 99 + one_to_ninetynine)
        three_hundreds = (len("threehundred") + len("threehundredand") * 99 + one_to_ninetynine)
        four_hundreds = (len("fourhundred") + len("fourhundredand") * 99 + one_to_ninetynine)
        five_hundreds = (len("fivehundred") + len("fivehundredand") * 99 + one_to_ninetynine)
        six_hundreds = (len("sixhundred") + len("sixhundredand") * 99 + one_to_ninetynine)
        seven_hundreds = (len("sevemhundred") + len("sevenhundredand") * 99 + one_to_ninetynine)
        eight_hundreds = (len("eighthundred") + len("eighthundredand") * 99 + one_to_ninetynine)
        nine_hundreds = (len("ninehundred") + len("ninehundredand") * 99 + one_to_ninetynine)

        one_to_onethousand = (
                    one_to_ninetynine + one_hundreds + two_hundreds + three_hundreds + four_hundreds + five_hundreds
                    + six_hundreds + seven_hundreds + eight_hundreds + nine_hundreds + len("onethousand"))

        return one_to_onethousand
