"""
Practical 4: Question 2
total_income.py
"""


# CONSTANTS
BORDER = "—" * 150
SENTINEL = -1


"""
Original Code:
def main():
    '''Display income report for incomes over a given number of months.'''
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
"""


"""
FUNCTIONS
"""


def main():
    """ The main function to display income reports for incomes over a given number of months. """
    print(BORDER)
    print("Practical 4: Question 2\ntotal_income.py")
    print(BORDER)
    incomes = []
    monthly_reports = get_number_of_monthly_reports()
    print(BORDER)
    for month in range(1, monthly_reports+1):
        income = get_income(month)
        incomes.append(income)
    print(BORDER)
    display_income_report(incomes)
    print(BORDER)


def get_number_of_monthly_reports():
    """ Get monthly reports from user. """
    run = 0
    while run != SENTINEL:
        try:
            months = int(input("How many monthly reports do you want?: "))
            if months >= 1:
                return months
            else:
                print("There must be at least 1 monthly report! Try again!")
        except ValueError:
            print("Invalid value! Try again!")


def get_income(month):
    """ Get income from user. """
    run = 0
    while run != SENTINEL:
        try:
            income = float(input(f"Enter income for month {month}: $"))
            if income >= 0:
                return income
            else:
                print("Income must be at least $0.00! Try again!")
        except ValueError:
            print("Invalid value! Try again!")


def display_income_report(incomes):
    """ Display income report based on the list of incomes """
    total = 0
    month_number = 0
    print("Income Report:")
    print(BORDER)
    for income in incomes:
        total += income
        month_number += 1
        print("Month {:2} – Income: ${:10.2f} Total: ${:10.2f}".format(month_number, income, total))


"""
PROGRAM
"""


main()
