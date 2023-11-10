#!/usr/bin/python3
"""In this code, I defined the Rectangle class that inherits from the Base class."""


from models.base import Base  # Import the Base class


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)  # Call the superclass constructor with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # List of setter and getter functions
    @property
    def width(self):
        """Gets the value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the vaue for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Gets the value for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Gets the value for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets value for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Gets value for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args):
        if len(args) > 0:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[2] if len(args) >= 3 else self.height
            self.x = args[3] if len(args) >= 4 else self.x
            self.y = args[4] if len(args) >= 5 else self.

    def update(self, *args, **kwargs):
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
