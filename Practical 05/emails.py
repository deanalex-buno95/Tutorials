"""
Practical 5: Question 4
emails.py
"""

# CONSTANTS
BORDER = "—" * 150
SENTINEL = -1


"""
MAIN FUNCTION
"""


def main():
    """ Main function to get emails and respective names into a dictionary """
    print(BORDER)
    print("Practical 5: Question 4\nemails.py")
    print(BORDER)
    run = 0
    email_dictionary = {}
    while run != SENTINEL:
        user_email = get_email()
        if user_email == "":
            run = SENTINEL
        else:
            user_name = get_name(user_email)
    print(BORDER)


"""
OTHER FUNCTIONS
"""


def get_email():
    """ Get email from user """
    run = 0
    while run != SENTINEL:
        user_email = input("Email: ").lower()
        if "@" in user_email or user_email == "":
            return user_email
        else:
            print("Invalid input! Try again!")


def get_name(user_email):
    """ Get name from the email of the user """
    name, domain = user_email.split("@")
    user_name = name.replace(".", " ")
    user_name = user_name.title()
    return user_name


"""
RUN MAIN FUNCTION
"""

if __name__ == '__main__':
    main()
