#!/usr/bin/python3
# 101-square.py by Elias joy chinonso

"""my square module."""


class Square:
    """defines a Square."""

    def __str__(self):
        """shows python to print the square my way"""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """ initialize the square with this
        Args:
            size: a side of square
            position: where the square is (coordinates)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """property of the length of a side of square
        Raises:
            TypeError: if size is not an int.
            ValueError: if size is < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size of square
        Args:
            value: the size
        Raises:
                TypeError: if value is not int
                ValueError: if valie < zero
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """property of the position of square
        Raises:
            TypeError: if value != tuple of 2 ints >= 0.
        Returns: the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position
        Args:
            value: where
        Raises:
                TypeError: if not tuple, ints, positive
        Returns: the position
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([a for a in value if isinstance(a, int) and a >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ area of square
        Returns:
            size * size
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns printed square with position"""
        pos = ""
        if not self.size:
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
        """print square."""
        print(self.pos_print(), end="")
