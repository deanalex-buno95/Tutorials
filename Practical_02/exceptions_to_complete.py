"""Question 5: Exceptions To Complete (exceptions_to_complete.py)"""


"""CONSTANTS"""


BORDER = "—" * 150


"""PROGRAM"""


print(BORDER)
print("Question 5: Exceptions To Complete (exceptions_to_complete.py)")
print(BORDER)

# variables for part 1:
is_finished = False
result = None

# part 1:
print("Part 1")
print(BORDER)

# try-except:
while not is_finished:  # repeat until the result is an integer
    try:  # normal
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:  # if the result input is not a number
        print("Please enter a valid integer.")
print("Valid result is:", result)

print(BORDER)
