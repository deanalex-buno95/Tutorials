"""Question 2: Random Numbers (randoms.py)"""


# modules:
import random


"""CONSTANTS"""


BORDER = "—" * 150


"""PROGRAM"""


print(BORDER)
print("Question 2: Random Numbers (randoms.py)")
print(BORDER)

# part 1:
print("Part 1")
print(BORDER)

# producing a random number between 1 and 100 inclusive:
print(random.randrange(1, 100))

print(BORDER)


"""OTHERS"""

'''
import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

line 1 — random.randint(5, 20): Smallest will be 5, largest will be 20
line 2 — random.randrange(3, 10, 2): Smallest will be 3, largest will be 9,
                                     won't be able to produce 4 since that number is skipped between 3 & 5
line 3 — random.uniform(2.5, 5.5): Smallest will be 2.5, largest will be 5.5
'''
