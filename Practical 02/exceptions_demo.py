"""Question 4: Exceptions Demo (exceptions_demo.py)"""


"""CONSTANTS"""


BORDER = "—" * 150


"""PROGRAM"""


print(BORDER)
print("Question 4: Exceptions Demo (exceptions_demo.py)")
print(BORDER)

# part 1:
print("Part 1")
print(BORDER)

# try-except (given):
try:  # normal
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:  # if the numerator or the denominator cannot be converted to integer type
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:  # if the denominator is 0
    print("Cannot divide by zero!")
print("Finished.")

print(BORDER)

# variables for part 2:
is_finished = False

# part 2:
print("Part 2")
print(BORDER)

# try-except (edited [remove 'ZeroDivisionError' exception]):
while not is_finished:
    try:  # normal
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            print("Cannot divide by zero!")
            denominator = int(input("Enter the denominator again: "))
        fraction = numerator / denominator
        print(fraction)
        is_finished = True
    except ValueError:  # if the numerator or the denominator cannot be converted to integer type
        print("Numerator and denominator must be valid numbers!")
print("Finished.")

print(BORDER)
