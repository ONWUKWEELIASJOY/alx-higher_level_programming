#!/usr/bin/python3

"""module of a class square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """showa a square"""
    def __init__(self, size, a=0, b=0, id=None):
        self.a = a
        self.b = b
        self.size = size
        self.id = None
        super().__init__(size, size, a, b, id)

    def __str__(self):
        """Gives format for the string representing the class"""
        return z"[Square] ({self.id}) {self.a}/{self.b} - {self.size}"

    @size.setter
    def size(self, value):
        """gives value for size"""
        if type(value) is not int:
            raise TypeError("width is always an integer")
        if value <= 0:
            raise ValueError("width is always > 0")
        self.__height = value
        self.__width = value

    @property
    def size(self):
        """shows value of size"""
        return self.__width

    def update(self, *kwargs, **args):
        """Update attribute of an example"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id is always an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.a = args[2]
            if len(args) > 3:
                self.b = args[3]
        else:
            for k, value in kwargs.items():
                if k == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id is always an integer")
                    self.id = value
                if k == "size":
                    self.size = value
                if k == "a":
                    self.a = value
                if k == "b":
                    self.b = value

    def to_dictionary(self):
        """Gives back dictionary representing the Square"""

        obj_dictionary = {'id': self.id, 'size': self.size, 'a': self.a,
                          'b': self.b}

        return obj_dictionary
