#!/usr/bin/python3
# Elias joy chinonso

"""This module inherits from the list class"""


class MyList(list):
    """The class that inherits from list"""
    def print_sorted(self):
        """This prints a sorted list"""
        print(sorted(self))
