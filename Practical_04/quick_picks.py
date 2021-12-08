"""
Practical 4: Question 6
quick_picks.py
"""


# MODULES
import random

# CONSTANTS
BORDER = "—" * 150
SENTINEL = -1
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


"""
FUNCTIONS
"""


def main():
    """ Main function for quick picks """
    print(BORDER)
    print("Practical 4: Question 6\nquick_picks.py")
    print(BORDER)
    quick_picks = []
    number_of_quick_picks = get_number_of_quick_picks()
    for i in range(number_of_quick_picks):
        quick_pick = []
        run = 0
        while run != SENTINEL:
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            if random_number not in quick_pick:
                quick_pick.append(random_number)
            if len(quick_pick) == 6:
                run = SENTINEL
        quick_picks.append(quick_pick)
    for number1, number2, number3, number4, number5, number6 in quick_picks:
        print("{:2} {:2} {:2} {:2} {:2} {:2}".format(number1, number2, number3, number4, number5, number6))
    print(BORDER)


def get_number_of_quick_picks():
    """ Get number of quick picks from user"""
    run = 0
    while run != SENTINEL:
        try:
            number_of_quick_picks = int(input("Get number of quick picks: "))
            if number_of_quick_picks >= 1:
                return number_of_quick_picks
            else:
                print("You must have at least 1 quick pick! Try again!")
        except ValueError:
            print("Invalid value! Try again!")


"""
PROGRAM
"""


if __name__ == '__main__':
    main()
