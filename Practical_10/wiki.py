"""
Practical 10:
Question 2
wiki.py
"""


import wikipedia


# CONSTANTS
BORDER = "—" * 150
SENTINEL = -1


def main():
    """
    Main function for the script
    :return: None
    """
    user_page = get_search_page()
    print(user_page.summary())


def get_search_page():
    user_input = input("Search: ")
    pages = wikipedia.search(user_input)
    for page in pages:
        print(page)

