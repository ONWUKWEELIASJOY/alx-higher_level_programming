#!/usr/bin/python3
# 6-square.py by Elias joy chinonso

"""My square module"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Create a Square
        Args:
            size: length of a side of Square
            position: where the square is (coordinates)
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """"The propery of size as the len of a side of Square
        Raises:
            TypeError: if size != int
            ValueError: if size < zero
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """property of the coordinates of this Square
        Raises:
            TypeError: if value != a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of this Square
        Args: value as a tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([a for a in value if isinstance(a, int) and a >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Gets area of a Square
        Returns: size squared
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for x in range(self.position[1]):
            pos += "\n"
        for x in range(self.size):
            for a in range(self.position[0]):
                pos += " "
            for b in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """prints square in position"""
        print(self.pos_print(), end='')
