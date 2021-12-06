"""
Practical 5: Question 1
state_names.py
"""


# CONSTANTS
BORDER = "—" * 150
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT" : "Northern Territory", "WA" : "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


"""
MAIN FUNCTION
"""


def main():
    """ Main function to get state name from state code input from dictionary 'CODE_TO_NAME' """
    print(BORDER)
    print("Practical 5: Question 1\nstate_names.py")
    print(BORDER)
    state_code = input("Enter short stage: ")
    while state_code != "":
        if state_code in CODE_TO_NAME:
            print(state_code, "is", CODE_TO_NAME[state_code])
        else:
            print("Invalid short state")
        state_code = input("Enter short stage: ")
    print(BORDER)


"""
RUN MAIN FUNCTION
"""


if __name__ == '__main__':
    main()
