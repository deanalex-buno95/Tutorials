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
        for filename in filenames:
            fixed_filename = get_fixed_filename(filename)
            # print(f"{filename}          {fixed_filename}")
            old_file_name = os.path.join(directory_name, filename)
            new_file_name = os.path.join(directory_name, fixed_filename)
            os.rename(old_file_name, new_file_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    i = 0
    run = 0
    while run != SENTINEL:
        if filename[i] == "." and filename[i+1:].lower() == "txt":  # convert extension to lowercase
            new_name += ("." + filename[i+1:].lower())
            run = SENTINEL
        elif filename[i].isupper() and filename[i-1].isupper() and i != 0:  # deal with 2 uppercase letters
            new_name += ("_" + filename[i])
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
    return new_name


main()
