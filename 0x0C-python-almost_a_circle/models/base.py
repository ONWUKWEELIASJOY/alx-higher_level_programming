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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        
        filename = cls.__name__ + ".json"
        
        with open(filename, "w") as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Creating a "dummy" Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Creating a "dummy" Square instance
        else:
            raise ValueError("Class not supported")

        dummy.update(**dictionary)  # Applying real values using the update method
        return dummy

    def update(self, *args, **kwargs):
        attributes = ["id", "width", "height", "size"]  # Define your attributes here
        if args:  # Assuming args correspond to the attribute values
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:  # kwargs correspond to the attribute names and values
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)


    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                data = file.read()
                if len(data) == 0:
                    return []
                else:
                    object_dicts = cls.from_json_string(data)
                    return [cls.create(**obj_dict) for obj_dict in object_dicts]
        except FileNotFoundError:
            return []


    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        new_instance = cls.create(id=int(row[0]), width=int(row[1]), height=int(row[2]), x=int(row[3]), y=int(row[4]))
                        instances.append(new_instance)
                    elif cls.__name__ == "Square":
                        new_instance = cls.create(id=int(row[0]), size=int(row[1]), x=int(row[2]), y=int(row[3]))
                        instances.append(new_instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        t = turtle.Turtle()

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.right(90)

        screen.mainloop()

