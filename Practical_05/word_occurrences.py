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
    display_word_occurrences_dictionary(word_occurrences_dictionary)
    print(BORDER)


"""
OTHER FUNCTIONS
"""


def get_word_occurrences_dictionary(input_text):
    """ Get all word occurrences from a string input into a dictionary """
    word_occurrences_dictionary = {}
    word = ""
    for char in input_text:
        if char.isalpha():
            word += char
        else:
            if word != "":
                if word in word_occurrences_dictionary:
                    word_occurrences_dictionary[word] += 1
                else:
                    word_occurrences_dictionary[word] = 1
                word = ""
    return word_occurrences_dictionary


def display_word_occurrences_dictionary(word_occurrences_dictionary):
    """ Display the word occurrences """
    if word_occurrences_dictionary == {}:
        print("No words!")
    else:
        longest_word_length = get_longest_word_length(word_occurrences_dictionary)
        for word in word_occurrences_dictionary:
            print("{0:{1}} : {2}".format(word, longest_word_length, word_occurrences_dictionary[word]))


def get_longest_word_length(word_occurrences_dictionary):
    """ Get longest word length of the word occurrences dictionary """
    longest_word_length = 0
    for word in word_occurrences_dictionary:
        word_length = len(word)
        if word_length > longest_word_length:
            longest_word_length = word_length
    return longest_word_length


"""
RUN MAIN FUNCTION
"""

if __name__ == '__main__':
    main()
