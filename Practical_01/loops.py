"""
Practical 1: Question 4
loops.py

Question:
Add loops for different ranges

Pseudocode:
Not Applicable
"""


"""
CONSTANTS
"""


BORDER = "—" * 150  # for cleaner output
SENTINEL = -1  # stopper for WHILE loops


"""
FUNCTIONS
"""


def display_numbers(first_number, last_number, steps=1):  # display numbers
    if last_number > first_number:
        for i in range(first_number, last_number+1, steps):
            if i == last_number:
                print(i)
            else:
                print(i, end=" ")
    else:
        for i in range(first_number, last_number-1, steps):
            if i == last_number:
                print(i)
            else:
                print(i, end=" ")


def display_stars(stars):  # display stars
    for i in range(stars):
        if i == stars-1:
            print("★")
        else:
            print("★", end="")


def display_rows_of_stars(rows_of_stars):  # display row of increasing stars
    for i in range(rows_of_stars):
        print("★" * (i+1))


"""
PROGRAMS
"""


print(BORDER)
display_numbers(1, 21, 2)  # display odd numbers from 1 to 21
print(BORDER)
display_numbers(0, 100, 10)  # display numbers from 0 to 100 via increments of 10
print(BORDER)
display_numbers(20, 1, -1)  # display numbers from 20 to 1
print(BORDER)
number_of_stars = 0
run = 0  # WHILE loop
while run != SENTINEL:
    number_of_stars_input = input("Number of stars: ")
    if number_of_stars_input.isdigit():
        if int(number_of_stars_input) >= 0:
            number_of_stars = int(number_of_stars_input)
            run = SENTINEL
        else:
            print("Invalid number!")
    else:
        print("Invalid value!")
display_stars(number_of_stars)  # display number of stars
print(BORDER)
number_of_rows = 0
run = 0  # WHILE loop
while run != SENTINEL:
    number_of_rows_input = input("Number of rows: ")
    if number_of_rows_input.isdigit():
        if int(number_of_rows_input) >= 0:
            number_of_rows = int(number_of_rows_input)
            run = SENTINEL
        else:
            print("Invalid number!")
    else:
        print("Invalid value!")
display_rows_of_stars(number_of_rows)  # display number of rows of increasing number of stars
print(BORDER)
