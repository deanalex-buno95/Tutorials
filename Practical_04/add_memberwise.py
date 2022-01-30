"""
Practice:
add_memberwise.py
"""


HEAD_INDEX = 0


def main():
    """ Main program. """
    print("Program started")
    list_i = [1, 2, 3]
    list_ii = [4, 5, 6]
    list_iii = [1, 2, 3]
    list_iv = [1, 2, 3, 4]
    test_list_alpha = add_memberwise(list_i, list_ii)
    test_list_beta = add_memberwise(list_iii, list_iv)
    print(f"add_memberwise({[1, 2, 3]}, {[4, 5, 6]})\n{test_list_alpha}")
    print(f"add_memberwise({[1, 2, 3]}, {[1, 2, 3, 4]})\n{test_list_beta}")
    print("Program ended")


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
