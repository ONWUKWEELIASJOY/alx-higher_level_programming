#!/usr/bin/python3
"""This module contains a square class"""

from models.rectangle import Rectangle  # Since Square inherits from Rectangle


class Square(Rectangle):
         """Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Gets the value of size"""
        return self.width  # Size of the square is the same as its width

    @size.setter
    def size(self, value):
        """Sets the value for size"""
        self.width = value
        self.height = value  # Assigning the same value to both width and height

    def update(self, *args, **kwargs):
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
