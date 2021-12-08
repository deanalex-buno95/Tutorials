"""
Practical 1: Question 2
sales_bonus.py

Question:
Program to calculate and display a user's bonus based on sales
(10% bonus for sales under $1000, 15% bonus otherwise)

Pseudocode:
SALES_UNDER_1000_BONUS_MULTIPLIER ← 0.1
SALES_AT_LEAST_1000_BONUS_MULTIPLIER ← 0.15
SENTINEL ← -1
\n\n
FUNCTION bonus(sales)
    IF sales >= 1000
        RETURN sales * SALES_AT_LEAST_1000_BONUS
    ELSE
        RETURN sales * SALES_UNDER_1000_BONUS
    ENDIF
\n\n
PRINT BORDER
run ← 0
REPEAT
    GET sales
    IF sales < 0
        run ← SENTINEL
    ELSE
        PRINT bonus(sales)
    PRINT BORDER
UNTIL run = SENTINEL
"""


"""
CONSTANTS
"""


BORDER = "—" * 150  # for a clean output
SALES_UNDER_1000_BONUS_MULTIPLIER = 0.1  # 10% bonus (< $1000 sales)
SALES_AT_LEAST_1000_BONUS_MULTIPLIER = 0.15  # 15% bonus (>= $1000 sales)
SENTINEL = -1  # stopper for WHILE loop


"""
FUNCTIONS
"""


def bonus(sales):  # get bonus from sales
    if sales >= 1000:  # 15% bonus
        return sales * SALES_AT_LEAST_1000_BONUS_MULTIPLIER
    else:  # 10% bonus
        return sales * SALES_UNDER_1000_BONUS_MULTIPLIER


"""
PROGRAM
"""


print(BORDER)
run = 0  # run WHILE loop
while run != SENTINEL:  # WHILE loop
    total_sales = float(input("Enter sales: $"))
    if total_sales <= 0:  # end WHILE loop
        run = SENTINEL
    else:  # PRINT sales_bonus
        sales_bonus = bonus(total_sales)
        print("Bonus: ${:.2f}".format(sales_bonus))
    print(BORDER)
