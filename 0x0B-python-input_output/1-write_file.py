#!/usr/bin/python3
# Elias joy Chinonso

"""This is a module that defines a file-writing function."""


def write_file(filename="", text=""):
    """This writes a string to a UTF8 text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
