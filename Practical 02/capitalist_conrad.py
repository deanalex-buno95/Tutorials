"""Question 3: Capitalist Conrad (capitalist_conrad.py)"""


# modules:
import random


"""CONSTANTS"""


BORDER = "—" * 150
MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0


"""PROGRAM"""


print(BORDER)
print("Question 3: Random Numbers (randoms.py)")
print(BORDER)

# variables for part 1:
price = INITIAL_PRICE

# part 1:
print("Part 1")
print(BORDER)

# writing the output after each price change:
print("${:,.2f}".format(price))
output_file = open("output_file.txt", "w")  # open 'output_file.txt'
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    if random.randint(1, 2) == 1:  # increase price
        price_change = random.uniform(0, MAX_INCREASE)  # price increase between 0 and MAX_INCREASE (float)
    else:  # decrease price
        price_change = random.uniform(-MAX_DECREASE, 0)  # price decrease between negative MAX_DECREASE and 0 (float)
    price *= (1 + price_change)  # updated price
    print("${:,.2f}".format(price))  # output on Python console
    output_file.write(f"${price:,.2f}\n")  # output on 'output_file.txt' file
output_file.close()  # close 'output_file.txt'


print(BORDER)
