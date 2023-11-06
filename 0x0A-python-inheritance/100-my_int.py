#!/usr/bin/python3
# Elias joy Chinonso

"""this is a module that defines a class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """Overrides == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Overrides != operator with == behavior"""
        return self.real == value
