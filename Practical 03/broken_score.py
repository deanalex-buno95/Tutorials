"""
Practical 3: Question 3
broken_score.py
"""

# imports

# CONSTANTS
BORDER = "—" * 150
SENTINEL = -1
MAXIMUM_SCORE = 100  # maximum valid score
MINIMUM_EXCELLENT_SCORE = 90  # minimum excellent score
MINIMUM_PASSABLE_SCORE = 50  # minimum passable score
MINIMUM_SCORE = 0  # minimum valid score

"""
Original Solution:
Practical 1: Question 3

print(BORDER)
score = float(input("Enter score: "))  # score
if MINIMUM_EXCELLENT_SCORE <= score <= MAXIMUM_SCORE:  # excellent
    print("Excellent!")
elif MINIMUM_PASSABLE_SCORE <= score < MINIMUM_EXCELLENT_SCORE:  # passable
    print("Passable!")
elif MINIMUM_SCORE <= score < MINIMUM_PASSABLE_SCORE:  # bad
    print("Bad!")
else:  # invalid
    print("Invalid!")
print(BORDER)
"""


"""
FUNCTIONS
"""


def main():
    """ Create the main function to print the grade based on the score from the user """
    print(BORDER)
    print("Practical 3: Question 3")
    print(BORDER)
    score = get_score("Enter score: ")
    grade = get_grade(score)
    print(f"Your grade: {grade}")
    print(BORDER)


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


"""
FUNCTION CALL
"""


main()
