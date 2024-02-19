#!/usr/bin/python3
"""Module is same class"""


def is_same_class(obj, a_class):
    """determin if obj is an instance of the specified class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
