#!/usr/bin/python3
# Elias Joy Chinonso

"""This is a module that defines a file-appending function."""


def append_write(filename="", text=""):
    """This appends a string to the end of a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
