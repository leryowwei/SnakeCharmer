"""
    DESCRIPTION:
        This python script solves an assorted collection of 'Project Euler' coding challenges in one neat python module
        This is the official entry to the coding challenge by the SnakeCharmers team.

    USAGE:
        > Make yourself a cup of tea, sit back, take in a big lungful of anticipatory air and prepare to be amazed

        > Get your stopwatch ready - oh wait - the built in timer will record how long this program took to solve
         all of the miriad of problems.

        > Dust off your abacus - no need - the handy built in score recorder will track the sum of all the problems
         solved for you

        > Open the console/terminal in the folder above the python scripts and type:

                python SnakeCharmers <arg1>

            Where <arg1> is the name of your first primary school teacher, first pet or mothers maiden name.
            (N.B. This is an optional argument.)
            (N.N.B. This code is robust enough to run even if you make a typo in your teachers name)
            (N.N.N.B. GDPR and a lack of omniscience place limitations on this codes ability to validate the accuracy of
            information supplied as a command line argument)


    OUTPUTS:
        > A sequence of problem statements followed by solutions is printed to the screen
        > A running tally of the total difficulty score achieved is printed
        > A final difficulty score, total run-time, performance score and assorted stats on problems solved is printed


    ASSUMPTIONS:
        > Each sub-module follows the base class
        > Assumes all modules have actually been coded correctly to solve the problem statement and don't just
        spit back 'random(0,10000000,1)'
        > Difficulty score is calculated as sum(difficulty^1.5)
        > Performance score is calculated as
        > You are sitting comfortably

"""

import sys
import time

def main():

    if len(sys.argv) == 2:  # If the optional argument is given then
        print("Wow, I can't believe you actually read the doc string")
        print("However, SAFETY MOMENT \n "
              "Please think carefully about giving away personal data and if it is really necessary \n"
              "See https://infozone.snclavalin.com/en/files/documents/data-privacy-book_en.pdf for further info")

    elif len(sys.argv) > 2:  # If multiple arguments are given
        print("Too many arguments given. Please Read the docstring for usage")

    else:

        start_time = time.time()  # Start timer for performance score purpose
        difficulty_score = 0  # Difficulty score starts at zero
        problems_solved = 0  # Those problems aren't going to solve themselves

        # loop through all questions available
        for num in range(1, 744):
            try:
                module = __import__("ques_{}".format(num))
                q = getattr(module, "question_{}".format(num))()
                print("-----Question {}-----".format(num))
                print(q.problem_statement())
                q.start_timer()
                print("Answer: {}".format(q.solve()))
                print("Time spent {}s\n".format(q.time_spent()))
                print("Difficulty level {}, difficulty score for this problem is {}".format(q.problem_difficulty(), q.difficulty_score()))
                difficulty_score += q.difficulty_score()
                problems_solved += 1
            except ModuleNotFoundError:
                pass

        end_time = time.time()
        total_time = end_time - start_time
        performance_score = total_time/problems_solved
        print("------------------------")
        print("Total performance score {} (seconds per problem)\n".format(performance_score))
        print("Total difficulty score {} \n".format(difficulty_score))


if __name__ == '__main__':
    main()