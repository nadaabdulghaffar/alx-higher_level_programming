#!/usr/bin/python3
""" Module for my list"""


class MyList (list):
    """MyList class"""
    def print_sorted(self):
        """Method  that prints sorted list"""
        print(sorted(self))
