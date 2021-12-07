"""
Practical 5: Question 3
word_occurrences.py
"""

# CONSTANTS
BORDER = "—" * 150


"""
MAIN FUNCTION
"""


def main():
    """ Main function to count the word occurrences from a string """
    print(BORDER)
    print("Practical 5: Question 3\nword_occurrences.py")
    print(BORDER)
    input_text = input("Text: ").lower()
    word_occurrences_dictionary = get_word_occurrences_dictionary(input_text)


"""
OTHER FUNCTIONS
"""


def get_word_occurrences_dictionary(input_text):
    """ Get all word occurrences from a string input into a dictionary """
    word_occurrences_dictionary = {}
    word = ""
    for char in input_text:
        if char != " ":
            word += char
        else:
            if word != "":
                if word in word_occurrences_dictionary:
                    word_occurrences_dictionary[word] += 1
                else:
                    word_occurrences_dictionary[word] = 1
    return word_occurrences_dictionary


"""
RUN MAIN FUNCTION
"""

if __name__ == '__main__':
    main()
