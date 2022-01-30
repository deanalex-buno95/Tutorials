"""
Practice:
scores.py
"""


SENTINEL = -1
MAXIMUM_SCORE = 100  # maximum valid score
MINIMUM_EXCELLENT_SCORE = 90  # minimum excellent score
MINIMUM_PASSABLE_SCORE = 50  # minimum passable score
MINIMUM_SCORE = 0  # minimum valid score
TEXT_FILE_NAME = "results.txt"


def main():
    """ Main function for the program. """
    run = 0
    while run != SENTINEL:
        try:  # get number of scores
            number_of_scores = int(input("Number of scores: "))
        except ValueError:  # not an integer
            print("Invalid value! Try again!")
        else:
            if number_of_scores <= 0:  # invalid number of scores
                print("Invalid number of scores! Try again!")
            else:  # start asking for each score and write the output in a text file
                lines = []
                for i in range(number_of_scores):
                    score = get_score("Score: ")
                    grade = get_grade(score)
                    line = f"{score} is {grade}"
                    if i != number_of_scores-1:
                        line += "\n"
                    lines.append(line)
                with open(TEXT_FILE_NAME, "w") as file:
                    file.writelines(lines)
                run = SENTINEL


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


if __name__ == '__main__':
    main()
