"""
Practical 1: Question 3
broken_score.py

Question:
Debugging

Pseudocode:
Not Applicable
"""


"""
CONSTANTS
"""


BORDER = "—" * 150  # for a clean output
MAXIMUM_SCORE = 100  # maximum valid score
MINIMUM_EXCELLENT_SCORE = 90  # minimum excellent score
MINIMUM_PASSABLE_SCORE = 50  # minimum passable score
MINIMUM_SCORE = 0  # minimum valid score


"""
PROGRAM
"""


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
