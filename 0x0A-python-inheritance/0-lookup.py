#!/usr/bin/python3
""" look up Module"""


def lookup(obj):
    """ list attributes and methods of an object
    Args:
        obj: object list
    Return:
        list: list of attributes and methods
    """
    return dir(obj)
