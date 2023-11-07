#!/usr/bin/python3
# Elias Joy Chinonso

"""This module defines a class Student"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """This initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the Student"""
        return self.__dict__
