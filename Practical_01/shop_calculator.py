"""
Practical 1: Question 5
shop_calculator.py

Question:
Program for a shop calculator

Pseudocode:
Not Applicable
"""


"""
CONSTANTS
"""


BORDER = "—" * 150  # for cleaner output
MINIMUM_DISCOUNT_APPLIED_PRICE = 100  # 10% discount kicks in if the full price exceeds $100


"""
FUNCTIONS
"""


def final_price(full_price):
    if full_price > MINIMUM_DISCOUNT_APPLIED_PRICE:  # 10% off
        return full_price * 0.9
    return full_price  # full


"""
PROGRAM
"""


print(BORDER)
number_of_items = int(input("Number of items: "))
total_price = 0
for i in range(number_of_items):  # add price of items
    item_price = float(input("Price of item: $"))
    total_price += item_price
total_price = final_price(total_price)  # adjust final price
print("Total price for {} items is ${:.2f}!".format(number_of_items, total_price))  # display
