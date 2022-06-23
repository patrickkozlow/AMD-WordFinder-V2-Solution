"""
This file is used to manage the import and error checking of external documents.
"""

# Import necessary packages
import sys


# create_list takes parses an input dictionary file and returns a list of all words in the file.
def create_list(file: str) -> list[str]:
    """
    Creates a list from a txt file containing words separated by a new line
    :param file: string PATH to a .txt file
    :return: list of strings in the file
    """
    try:
        f = open(file, 'r')
    except FileNotFoundError:
        print(f"File {file} not found.")
        sys.exit()
    except OSError:
        print(f"Error occurred trying to open {file}")
        sys.exit()
    except Exception as err:
        print(f"Unexpected error opening {file}", repr(err))
        sys.exit()
    else:
        with f:
            content = f.read()
            ls = content.split("\n")
            return ls


# create_grid takes parses an input grid file and returns a list representing a grid with size.
def create_grid(file: str) -> list[list[str]]:
    """
    Creates a matrix that contains the grid size and contents from a .txt file
    :param file: string PATH to a .txt file
    :return: An matrix of lowercase characters
    """
    try:
        f = open(file, 'r')
    except FileNotFoundError:
        print(f"File {file} not found.")
        sys.exit()
    except OSError:
        print(f"Error occurred trying to open {file}")
        sys.exit()
    except Exception as err:
        print(f"Unexpected error opening {file}", repr(err))
        sys.exit()
    else:
        with f:
            # create board with lowercase str and '\n' removed
            board = [[str(c).strip().lower() for c in line.split(' ')] for line in f]
            return board
