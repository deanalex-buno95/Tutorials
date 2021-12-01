"""
Practical 4: Question 4
list_exercises.py
"""


# CONSTANTS
BORDER = "—" * 150
SENTINEL = -1


"""
FUNCTIONS
"""


def main():
    """ Main function for 2 list exercises """
    print(BORDER)
    print("Practical 4: Question 5\nlist_exercises.py")
    print(BORDER)
    print("Part 1:")
    number_list = get_list_of_numbers()
    display_output(number_list)
    print(BORDER)
    print("Part 2:")
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    input_username = get_username()
    print(access_allowed(usernames, input_username))
    print(BORDER)


def get_list_of_numbers():
    """ Get a list of 5 numbers from the user """
    number_list = []
    for i in range(5):
        number = get_number()
        number_list.append(number)
    return number_list


def get_number():
    """ Get a number from the user """
    run = 0
    while run != SENTINEL:
        try:
            number = int(input("Number: "))
            return number
        except ValueError:
            print("Invalid value! Try again!")


def display_output(number_list):
    """ Display outputs from 'number_list' """
    first_number = number_list[0]
    last_number = number_list[-1]
    smallest_number = min(number_list)
    largest_number = max(number_list)
    average_of_numbers = sum(number_list) / len(number_list)
    print(f"The first number is {first_number}")
    print(f"The last number is {last_number}")
    print(f"The smallest number is {smallest_number}")
    print(f"The largest number is {largest_number}")
    print(f"The average of the numbers is {average_of_numbers}")


def get_username():
    """ Get username from the user """
    username = input("Username: ")
    return username


def access_allowed(usernames, input_username):
    """ Give boolean to represent granted or denied access (True/False) from username list and input username """
    return "Access Granted!" if (input_username in usernames) else "Access Denied!"


"""
PROGRAM
"""


main()
