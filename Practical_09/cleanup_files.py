"""
Practical 9:
Question 2
"""


# import shutil
import os

SENTINEL = -1


def main():
    """Main function for cleaning up file names."""

    # Starting directory
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir("Lyrics")

    # Walk
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        # Add a loop to rename the files
        """
        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)
        """
        for i, filename in enumerate(filenames):
            print(i, filename)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    i = 0
    run = 0
    while run != SENTINEL:
        if filename[i] == ".":  # convert extension to lowercase
            new_name += ("." + filename[i+1:].lower())
            run = SENTINEL
        elif filename[i] == " " or filename[i] == "_":  # convert space to underscore or concatenate the underscore
            new_name += "_"
            if filename[i+1].islower():  # next char is a lowercase letter
                new_name += filename[i+1].upper()
                i += 1  # avoid adding duplicate character
            elif filename[i+1].isupper():  # next char is an uppercase letter
                new_name += filename[i+1]
                i += 1  # avoid adding duplicate character
        elif filename[i] == "(":
            new_name += (filename[i] + filename[i+1].upper())
            i += 1  # avoid adding duplicate character
        elif filename[i].islower() and filename[i+1].isupper():  # deal with PascalCase
            new_name += (filename[i] + "_" + filename[i+1])
            i += 1  # avoid adding duplicate character
        else:  # none of the special cases
            new_name += filename[i]
        i += 1
    # new_name = filename.replace(".TXT", ".txt")
    return new_name


# main()
for text_file in ["Away In A Manger.txt",
                  "SilentNight.txt",
                  "O little town of bethlehem.TXT",
                  "ItIsWell (oh my soul).txt",
                  "Away_In_A_Manger.txt",
                  "Silent_Night.txt",
                  "O_Little_Town_Of_Bethlehem.txt",
                  "It_Is_Well_(Oh_My_Soul).txt"]:
    print(get_fixed_filename(text_file))
