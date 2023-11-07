#!/usr/bin/python3
# Elias Joy Chinonso

"""This is a module that defines a Python class-to-JSON function"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure"""
    return obj.__dict__
