#!/usr/bin/python3

"""In this code, we define the Base class with a private class attribute __nb_objects initialized to 0."""

"""The class has a constructor __init__ which handles the logic for assigning the id attribute based on the provided requirements."""


import csv
import json
import os
import turtle


class Base:
    """This Base class can be imported and used as the base class for       other classes
    """ 
    """in your project, providing consistent ID management functional       ity.
    """

    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """ """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

