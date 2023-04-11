#!/usr/bin/python3
"""
  This function takes an object as input and returns a list of attributes and methods available for the object.
"""
def lookup(obj):
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) or '__' not in attr]
