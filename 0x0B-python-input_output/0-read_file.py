#!/usr/bin/python3
# Elias joy Chinonso

"""This is a module that defines a text file-reading function"""


def read_file(filename=""):
    """This prints out the contents of a UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
