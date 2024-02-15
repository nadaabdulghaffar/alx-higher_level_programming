#!/usr/bin/python3
"""Square Module"""


class Square:
    """Defines Square Class"""
    def __init__(self, size=0):
        """Constructor
        Args:
            size: length of side of the square (default 0)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of the square
            Return: The Area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Retireve length size
            Return: size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ prints in stdout the square with the character #"""
        for length in range(self.__size):
            for width in range(self.__size):
                print("#", end="")
            print()
