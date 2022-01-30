"""
Practice:
add_memberwise
"""


HEAD_INDEX = 0
LIST_1 = []
LIST_2 = []


def main():
    """ Main program. """
    pass


def add_memberwise(list_1, list_2):
    """ Add values of two lists, memberwise (same index). """
    if not list_1 and not list_2:  # base case 1: both list_1 and list_2 are empty
        return []
    elif not list_1:  # base case 2: list_1 is empty
        return list_2
    elif not list_2:  # base case 3: list_2 is empty
        return list_1
    else:  # general case/recursive call: neither list_1 nor list_2 are empty
        element_1 = list_1.pop(HEAD_INDEX)
        element_2 = list_2.pop(HEAD_INDEX)
        sum_of_elements = element_1 + element_2
        return [sum_of_elements] + add_memberwise(list_1, list_2)


if __name__ == "__main__":
    main()
