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
    print(BORDER)
    print("Welcome to Wikipedia Lite")
    print(BORDER)
    run = 0
    while run != SENTINEL:
        user_page = get_search_page()
        if user_page == "":
            run = SENTINEL
        else:
            print(BORDER)
            print(wikipedia.summary(user_page))
        print(BORDER)


def get_search_page():
    """
    Get search page from user
    :return: "" or wikipedia.page
    """
    user_input = input("Search: ")
    if user_input == "":
        return ""
    available_pages = wikipedia.search(user_input)
    for i, page in enumerate(available_pages):
        print(f"{i} → {page}")
    run = 0
    while run != SENTINEL:
        try:  # get user page
            user_page_number = get_page_number()
            user_page = wikipedia.page(available_pages[user_page_number])
        except IndexError:  # page number does not exist
            print("Page number does not exist!")
        except wikipedia.DisambiguationError:  # page is a disambiguation page
            print("This is a disambiguation page! Please try again!")
        except wikipedia.PageError:  # the page id does not work
            print("Currently, this wikipedia page is unavailable! Please try again!")
        else:
            return user_page


def get_page_number():
    """
    Get user page number from user
    :return: int
    """
    run = 0
    while run != SENTINEL:
        try:
            page_number = int(input("Get page number: "))
        except ValueError:
            print("Invalid page number!")
        else:
            return page_number


if __name__ == '__main__':
    main()
