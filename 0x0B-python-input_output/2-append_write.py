#!/usr/bin/python3
"""Define append_write methode"""


def append_write(filename="", text=""):
    """ append a string to a text file
        Return: the number of characters
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
