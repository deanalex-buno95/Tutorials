"""
Practice:
scores.py
"""


SENTINEL = -1
MAXIMUM_SCORE = 100  # maximum valid score
MINIMUM_EXCELLENT_SCORE = 90  # minimum excellent score
MINIMUM_PASSABLE_SCORE = 50  # minimum passable score
MINIMUM_SCORE = 0  # minimum valid score


def main():
    """ Main function for the program. """
    pass


def get_score(prompt):
    """ Get the score from the user """
    run = 0
    while run != SENTINEL:
        try:
            score = float(input(prompt))
            if MINIMUM_SCORE <= score <= MAXIMUM_SCORE:
                return score
            print("Invalid score! Try again!")
        except ValueError:
            print("Invalid value! Try again!")


def get_grade(score):
    """ Get the grade based on the score from the user """
    if score >= MINIMUM_EXCELLENT_SCORE:
        return "Excellent"
    elif score >= MINIMUM_PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"
