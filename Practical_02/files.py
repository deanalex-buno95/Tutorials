"""Question 6: Files (files.py)"""


"""CONSTANTS"""


BORDER = "—" * 150


"""PROGRAM"""


print(BORDER)
print("Question 6: Files (files.py)")
print(BORDER)

# variables for parts 1 and 2:
name_file = "name.txt"

# parts 1 and 2:
print("Parts 1 and 2")
print(BORDER)

# asking for name and writing it on a file
name = input("Your name: ").title()
with open(name_file, "w") as file:
    file.write(name)

# reading 'name.txt' file and printing statement
with open(name_file) as file:
    name = file.readline()
    print(f"Your name is {name}!")

print(BORDER)

# variables for parts 3 and 4:
numbers_file = "numbers.txt"
total_first_2_numbers = 0
total_all_numbers = 0

# parts 3 and 4:
print("Parts 3 and 4")
print(BORDER)

# reading 'numbers.txt' and summing first 2 numbers
with open(numbers_file) as file:
    for i, line in enumerate(file, 1):
        if i > 2:
            break
        else:
            number = int(line.strip())
            total_first_2_numbers += number
print(f"Total of the first 2 numbers is: {total_first_2_numbers}!")

# reading 'numbers.txt' and summing all numbers
with open(numbers_file) as file:
    lines = file.readlines()
    for line in lines:
        number = int(line.strip())
        total_all_numbers += number
print(f"Total of the numbers is: {total_all_numbers}!")

print(BORDER)
