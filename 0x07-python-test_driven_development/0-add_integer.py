#!/usr/bin/python3
""" Define add_integer Module"""


import math

def add_integer(a, b=98):
    """function that adds 2 integers.
        Raise:
            TypeError if a or b not int or float
            ValueError if a or b is NaN
            OverflowError if a or b is too large
        return:
            sum of two number
        """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")

    if math.isnan(a) or math.isnan(b):
        raise ValueError()

    if math.isinf(a) or math.isinf(b):
        raise OverflowError()
    
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
