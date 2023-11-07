#!/usr/bin/python3
# Elias Joy Chinonso

"""This is a module that defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object"""
    return json.dumps(my_obj)
