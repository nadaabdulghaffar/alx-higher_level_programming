#!/usr/bin/python3
"""Define read_file methode"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it"""
    with open(filename, encoding="utf-8") as file:
        content=file.read()
        print(content, end="")
