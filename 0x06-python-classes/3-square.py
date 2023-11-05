#!/usr/bin/python3
# 0-square.py by Elias joy chinonso

"""module that defines a square """


class Square:
    """class that represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represnet the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculates area of the square
        Returns: square of the size
        """

        return (self.__size ** 2)
