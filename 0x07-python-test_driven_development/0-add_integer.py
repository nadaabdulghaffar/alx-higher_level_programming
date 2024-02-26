#!/usr/bin/python3
""" Define add_integer Module"""


def add_integer(a, b=98):
    """function that adds 2 integers.
        Raise:
            TypeError if a or b not int or float
        return:
            sum of two numbers
        """
    if type(a) not in (float, int):
        raise TypeError("a must be an integer")
    if type(b) not in (float, int):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
