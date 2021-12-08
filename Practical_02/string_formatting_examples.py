"""Question 1: String Formatting (string_formatting_examples.py)"""


"""CONSTANTS"""


BORDER = "—" * 150


"""PROGRAM"""


print(BORDER)
print("Question 1: String Formatting (string_formatting_examples.py)")
print(BORDER)

# variables for part 1:
name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

# part 1:
print("Part 1")
print(BORDER)

# the manual way of formatting text (using string concatenation):
print("My guitar: " + name + ", was first made in " + str(year) + "!")

# the first special way of formatting text (using 'str.format()'):
print("My guitar: {}, was first made in {}!".format(name, year))
print("My guitar: {0}, was first made in {1}!".format(name, year))
print("My guitar: {0}, was first made in {1} (Yeah! {1}!)!".format(name, year))

# the second special way of formatting text (using f-string formatting [f""]):
print(f"My {name} was first made in {year} (Yeah! {year}!)!")

# formatting currency (grouping with comma, round to 2 decimal places):
print("My {} would cost ${:,.2f}!".format(name, cost))
print(f"My {name} would cost ${cost:,.2f}!")

print(BORDER)

# variables for part 2:
numbers = [1, 19, 123, 456, -25]

# part 2:
print("Part 2")
print(BORDER)

# aligning columns:
for number in numbers:
    print("Number is {:>5}!".format(number))

# using f-string and enumerate function for indices:
for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:>5}!")

print(BORDER)

# part 3:
print("Part 3")
print(BORDER)

# part 3a (producing statement):
print(f"{year} {name} for about ${cost:,.2f}!")

# part 3b (producing right-aligned numbers):
for i in range(0, 151, 50):
    print(f"{i:>3}")

print(BORDER)
