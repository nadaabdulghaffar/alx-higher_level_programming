#!/usr/bin/python3
"""Define write_file methode"""


def write_file(filename="", text=""):
    """ writes a string to a text file
        Return: the number of characters
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
        
