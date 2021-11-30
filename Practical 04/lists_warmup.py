"""
Practical 4: Question 1
lists_warmup.py
"""


# CONSTANTS
BORDER = "—" * 150


"""
FUNCTIONS
"""


def main():
    """ The main function to output answers for each expression and mutate list of numbers """
    print(BORDER)
    print("Practical 4: Question 1\nlists_warmup.py")
    print(BORDER)
    print("Expressions:")
    print(f"         numbers[0]:   {numbers[0]}")  # 3
    print(f"        numbers[-1]:   {numbers[-1]}")  # 2
    print(f"         numbers[3]:   {numbers[3]}")  # 1
    print(f"       numbers[:-1]:   {numbers[:-1]}")  # [3, 1, 4, 1, 5, 9]
    print(f"       numbers[3:4]:   {numbers[3:4]}")  # [1]
    print(f"       5 in numbers:   {5 in numbers}")  # True
    print(f"       7 in numbers:   {7 in numbers}")  # False
    print(f"     '3' in numbers: {'3' in numbers}")  # False
    print(f"numbers + [6, 5, 3]: {numbers + [6, 5, 3]}")  # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(BORDER)
    print("Mutations:")
    print(f"Change the first element of numbers to 'ten' (the string, not the number 10): numbers[0] = 'ten'")
    numbers[0] = "ten"
    print(f"                                     Change the last element of numbers to 1: numbers[-1] = 1")
    numbers[-1] = 1
    print(f"              Get all the elements from numbers except the first two (slice): numbers[2:]")
    new_number_list = numbers[2:]
    print(new_number_list)
    print(f"                                         Check if 9 is an element of numbers: 9 in numbers")
    check_9_in_numbers = 9 in numbers
    print(check_9_in_numbers, f"Expected: {9 in numbers}")
    print(BORDER)


"""
PROGRAM
"""


numbers = [3, 1, 4, 1, 5, 9, 2]


main()
