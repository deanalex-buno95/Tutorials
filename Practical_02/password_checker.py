"""Question 7: Password Checker (password_checker.py)"""


"""CONSTANTS"""


BORDER = "—" * 150
SPECIAL_CHARACTERS = " !@#$%^&*()_-=+`~,./'[]<>?{}|\\"
SENTINEL = -1


"""FUNCTIONS"""


def correct_length(password, shortest_length, longest_length):  # correct password length
    return shortest_length <= len(password) <= longest_length


def has_lower(password):  # check if there is at least 1 lowercase character
    for char in password:
        if char.islower():
            return True
    return False


def has_upper(password):  # check if there is at least 1 uppercase character
    for char in password:
        if char.isupper():
            return True
    return False


def has_digit(password):  # check if there is at least 1 numerical character
    for char in password:
        if char.isdigit():
            return True
    return False


def has_special(password):  # check if there is at least 1 special character
    for char in password:
        if char in SPECIAL_CHARACTERS:
            return True
    return False


def password_checker_part1(password):  # password check for part 1
    return correct_length(password, 5, 15) and has_lower(password) and has_upper(password) and has_digit(password) and has_special(password)


def password_checker_part2(password):  # password check for part 2
    return correct_length(password, 2, 6) and has_lower(password) and has_upper(password) and has_digit(password)


"""PROGRAM"""


print(BORDER)
print("Question 7: Password Checker (password_checker.py)")
print(BORDER)

# part 1:
print("Part 1")
print(BORDER)

# validate password (first type):
run_part_1 = 0
print("Please enter a valid password!")
print("Your password must be between 5 and 15 characters, and contain:")
print("•   1 or more uppercase characters")
print("•   1 or more lowercase characters")
print("•   1 or more numbers")
print("•   1 or more special characters ( !@#$%^&*()_-=+`~,./'[]<>?{}|\\)")
while run_part_1 != SENTINEL:
    user_password = input("> ")
    if password_checker_part1(user_password):
        print(f"Your {len(user_password)}-character password is valid: {user_password}")
        run_part_1 = SENTINEL
    else:
        print("Invalid password!")

print(BORDER)

# part 2:
print("Part 2")
print(BORDER)

# validate password (second type):
run_part_2 = 0
print("Please enter a valid password!")
print("Your password must be between 2 and 6 characters, and contain:")
print("•   1 or more uppercase characters")
print("•   1 or more lowercase characters")
print("•   1 or more numbers")
while run_part_2 != SENTINEL:
    user_password = input("> ")
    if password_checker_part2(user_password):
        print(f"Your {len(user_password)}-character password is valid: {user_password}")
        run_part_2 = SENTINEL
    else:
        print("Invalid password!")

print(BORDER)
