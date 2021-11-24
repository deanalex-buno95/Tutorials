"""
Practical 1: Question 6
menus.py

Question:
Menu creation

Pseudocode:
Not Applicable
"""


"""
CONSTANTS
"""


BORDER = "—" * 150  # for cleaner output
SENTINEL = -1  # end menu
CHOICES = ["H", "G", "Q"]  # available choices


"""
PROGRAM
"""


name = input("Your name: ").title()
run = 0  # run menu
print(BORDER)
while run != SENTINEL:  # menu
    print("Menu:")
    print("(H): Hello")
    print("(G): Goodbye")
    print("(Q): Quit")
    print(BORDER)
    choice = input("Choice: ").upper()
    while choice not in CHOICES:  # validate choice
        print("Invalid choice!")
        choice = input("Choice: ").upper()
    print(BORDER)
    if choice == "H":  # hello
        print(f"Hello, {name}!")
    elif choice == "G":  # goodbye
        print(f"Goodbye, {name}!")
    else:  # quit
        print("Program ended!")
        run = SENTINEL
    print(BORDER)
