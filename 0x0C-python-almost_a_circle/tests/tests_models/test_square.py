#!/usr/bin/python3

import sys
import io
import os
import json
import unittest
import contextlib
from models.base import Base
import inspect
from contextlib import redirect_stdout
from models.square import Square
from io import StringIO
from models.rectangle import Rectangle

""""Run test case for module square"""

class test_square(unittest.TestCase):
        """checking square"""

    def setUp(self):
        """Initializing example with width and height
            parameters"""
        self.sq = Square(5)

    def tearDown(self):
        """Deleting created example"""
        try:
            os.remove("Square.json")
        except:
            pass
        del self.sq

    def test_asquare_id(self):
        """check the id for square"""
        squ = Square(2, 0, 0, 199)
        self.assertEqual(199, squ.id)

    def test_width_string(self):
        """ checking for other than int"""
        with self.assertRaises(TypeError):
            squ = Square("1")

    def test_width_bool(self):
        """checking for other than int"""
        with self.assertRaises(TypeError):
            squ = Square(True)

    def test_width_list(self):
        """checking for other than int"""
        with self.assertRaises(TypeError):
            squ = Square([10, 6])

    def test_a_string(self):
        """checking for other than int"""
        with self.assertRaises(TypeError):
            squ = Square(1, "46")

    def test_a_bool(self):
        """checking for other than int"""
        with self.assertRaises(TypeError):
            squ = Square(1, True)

    def test_a_list(self):
        """checking for other than int"""
        with self.assertRaises(TypeError):
            squ = Square(1, [10, 6])

    def test_b_string(self):
        """checking for other than int"""
        with self.assertRaises(TypeError):
            squ = Square(1, 7, "46")

    def test_b_bool(self):
        """checking for other than int"""
        with self.assertRaises(TypeError):
            squ = Square(1, 7, True)

    def test_b_list(self):
        """checking for other than int"""
        with self.assertRaises(TypeError):
            squ = Square(1, 7, [10, 6])

    def test_width_negative(self):
        """checking with negative int"""
        with self.assertRaises(ValueError):
            squ = Square(-4)

    def test_a_negative(self):
        """checking with negative int"""
        with self.assertRaises(ValueError):
            squ = Square(4, -3)

    def test_b_negative(self):
        """checking with negative int"""
        with self.assertRaises(ValueError):
            squ = Square(4, 2, -3)

    def test_width_zero(self):
        """checking with negative int"""
        with self.assertRaises(ValueError):
            squ = Square(0, 5)

    def test_width_float(self):
        """checking for other than int"""
        with self.assertRaises(TypeError):
            squ = Square(1.07, 5)

    def test_a_float(self):
        """checking for other than int"""
        with self.assertRaises(TypeError):
            squ = Square(5, 1.07)

    def test_b_float(self):
        """checking for other than int"""
        with self.assertRaises(TypeError):
            squ = Square(5, 8, 1.07)

    def test_width(self):
        """checking the square width getter"""
        self.assertEqual(5, self.sq.width)

    def test_height(self):
        """checking the square height getter"""
        self.assertEqual(5, self.sq.height)

    def test_a(self):
        """checking square a getter and setter"""

        self.sq.a = 54
        self.assertEqual(54, self.sq.a)
        self.assertEqual(0, self.sq.b)

    def test_b(self):
        """checking square b getter and setter"""

        self.sq.b = 45
        self.assertEqual(45, self.sq.b)
        self.assertEqual(0, self.sq.a

    def test_area(self):
        """checking the area of the square"""
        self.assertEqual(self.sq.area(), 5 * 5)
        squ = Square(3, 8, 8, 2)
        self.assertEqual(squ.area(), 3 * 3)

    def test_str_overload(self):
        sq = Square(5, 8, 7, 88)
        self.assertEqual(sq.__str__(), "[Square] (88) 8/7 - 5")

    def test_update_id(self):
        """checking the update method"""
        self.sq.update(54)
        self.assertEqual(54, self.sq.id)

    def test_update_width(self):
        """checking the update method"""
        self.sq.update(54, 30)
        self.assertEqual(5, self.sq.width)

    def test_update_height(self):
        """checking the update method"""
        self.sq.update(54, 10)
        self.assertEqual(5, self.sq.height)

    def test_update_a(self):
        """checking the update method"""
        self.sq.update(54, 30, 10)
        self.assertEqual(10, self.sq.a)

    def test_update_b(self):
        """checking the update method"""
        self.sq.update(54, 30, 6, 2)
        self.assertEqual(2, self.sq.b)

    def test_update_dict(self):
        """checking the update method with **kwargs"""
        self.sq.update(b=1, size=2, a=3, id=89)
        self.assertEqual(1, self.sq.b)
        self.assertEqual(2, self.sq.size)
        self.assertEqual(3, self.sq.a)
        self.assertEqual(89, self.sq.id)

    def test_update_dict_list(self):
        """checking the update method with **kwargs and *args"""
        self.sq.update(1000, b=1, width=2, a=3, id=89)
        self.assertEqual(1000, self.sq.id)

    def test_update_dict_no_key(self):
        """checking the update method with **kwargs"""
        self.sq.update(b=1, size=2, aoa=3, id=89)

    def test_update_string(self):
        """checking the update method with **kwargs"""
        # self.assertEqual(self.sq.id, "str")
        with self.assertRaises(TypeError):
           self.sq.update("str") 

    def test_to_dict(self):
        """checking the type that is returned from the to_dictionary method"""
        rec1 = Square(5)
        self.assertEqual(type(rec1.to_dictionary()), dict)

    def test_to_dict_print(self):
        """checking the dict that will be printed"""
        rec1 = Square(5, 0, 0, 410)
        rec1_dict = rec1.to_dictionary()
        self.assertEqual(rec1_dict,
                         {'size': 5, 'id': 410, 'a': 0, 'b': 0})

    def test_missing_height(self):
        """waiting for a type error because height and width are missing"""
        with self.assertRaises(TypeError):
            Square()

    def test_saving_to_file(self):
        """checking saving a file into json format"""
        try:
            os.remove("Square.json")
        except:
            pass
        rec1 = Square(5, 0, 0, 346)
        Square.save_to_file([rec1])

        with open("Square.json", "m") as file:
            content = file.read()
        u = [{"id": 346, "a": 0, "size": 5, "b": 0}]
        self.assertEqual(u, json.loads(content))

    def test_saving_to_file_no_iter(self):
        """moving a non iterable to the function"""
        with self.assertRaises(TypeError):
            Square.save_to_file(self.sq)

    def test_saving_to_file_None(self):
        """checking saving a file into json format sending None"""
        try:
            os.remove("Square.json")
        except:
            pass
        rec1 = Square(5, 0, 0, 346)
        Square.save_to_file(None)

        with open("Square.json", "m") as file:
            content = file.read()

        self.assertEqual("[]", content)

    def test_saving_to_file_type(self):
        """checks saving a file into json format and testing the type"""
        try:
            os.remove("Square.json")
        except:
            pass
        rec1 = Square(5, 0, 0, 346)
        Square.save_to_file([rec1])

        with open("Square.json", "m") as file:
            content = file.read()

        self.assertEqual(str, type(content))
        try:
            os.remove("Square.json")
        except:
            pass

    def test_json_string_type(self):
            """checking the returned type"""
            list_input = [
                {'id': 2089, 'size': 10},
                {'id': 2712, 'size': 1}]
            json_list_input = Square.to_json_string(list_input)
            list_output = Square.from_json_string(json_list_input)
            self.assertEqual(type(list_input), list)

    def test_json_string(self):
            """checking that the json string gets converted into a list"""
            list_input = [
                {'id': 2089, 'size': 10},
                {'id': 2712, 'size': 7}]
            json_list_input = Square.to_json_string(list_input)
            list_output = Square.from_json_string(json_list_input)
            sq1 = {'id': 2089, 'size': 10}
            sq2 = {'size': 7, 'id': 2712}
            self.assertEqual(list_input[0], sq1)
            self.assertEqual(list_input[1], sq2)

    def test_dict_to_instance(self):
        """checks that an instance is created from a dict"""
        rec1 = Square(5)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Square.create(**rec1_dictionary)
        self.assertNotEqual(rec1, rec2)

    def test_isnot_dict_to_instance(self):
        """checks that an instance is created from a dict"""
        rec1 = Square(109)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Square.create(**rec1_dictionary)
        self.assertIsNot(rec1, rec2)

    def test_load_from_file_not_the_same(self):
        """checking that an object was created from the
            list but has a different adress."""
        rec1 = Square(10)
        list_squares_input = [rec1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertNotEqual(id(rec1), id(list_squares_output[0]))

    def test_load_from_file_same_width(self):
        """Trying that an object was created from the
            list and has the same witdh
        """
        rec1 = Square(10)
        list_squares_input = [rec1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertEqual(rec1.width, list_squares_output[0].size)

    def test_load_from_file_same_height(self):
        """checking that an object was created from the
            list and has the same height"""
        rec1 = Square(10)
        list_squares_input = [rec1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertEqual(rec1.size, list_squares_output[0].size)

    def test_load_from_file_same_a(self):
        """
            trying that an object was created from the
            list and has the same a"""
        rec1 = Square(10, 2, 8)
        list_squares_input = [rec1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertEqual(rec1.a, list_squares_output[0].a)

    def test_load_from_file_same_b(self):
        """trying that an object was created from the
            list and has the same n"""
        rec1 = Square(10, 2, 8)
        list_squares_input = [rec1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertEqual(rec1.b, list_squares_output[0].b)

    def test_display_square(self):
        """trying the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        rec1 = Square(10)
        rec1.display()
        sys.stdout = sys.__stdout__

        output = ("##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n")
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_one(self):
        """chesks the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        rec1 = Square(1)
        rec1.display()
        sys.stdout = sys.__stdout__

        output = ("#\n")
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_zero(self):
        """Checks the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        rec1 = Square(3)
        rec1.display()
        sys.stdout = sys.__stdout__

        output = '###\n###\n###\n'
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square(self):
        """Checks the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        rec1 = Square(10)
        rec1.display()
        sys.stdout = sys.__stdout__

        output = ("##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n")
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_one(self):
        """Checks the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        rec1 = Square(1)
        rec1.display()
        sys.stdout = sys.__stdout__

        output = ("#\n")
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_zero(self):
        """checks the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        rec1 = Square(3)
        rec1.display()
        sys.stdout = sys.__stdout__

        output = '###\n###\n###\n'
        self.assertEqual(capturedOutput.getvalue(), output)

class TestSquare(unittest.TestCase):
    """class for checking Square class method"""

    @classmethod
    def setUpClass(cls):
        """Setup class method for doc tests"""
        cls.setup = inspect.getmembers(Square, inspect.isfunction)

    def test_module_docstring(self):
        """checks if module docstring documentation exist"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_class_docstring(self):
        """checks if class docstring documentation exist"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_wrong_inputted_values(self):
        """checks for negative and zero values"""
        with self.assertRaises(ValueError):
            Sq = Square(0, 0)
        with self.assertRaises(ValueError):
            Sq = Square(-4, -5)
        with self.assertRaises(ValueError):
            Sq = Square(1, 1, -2, -2)
        with self.assertRaises(TypeError):
            Sq = Square()
        with self.assertRaises(TypeError):
            Sq = Square(1, 2, 3, 4, 5, 6, 7)

    def test_inputted_types(self):
        """different variety for inputted arguments"""
        with self.assertRaises(TypeError):
            Sq = Square('width', 'height')
        with self.assertRaises(TypeError):
            Sq = Square(2.4, 1.3)
        with self.assertRaises(TypeError):
            Sq = Square(1, 2, 'a value', 'b value')
        with self.assertRaises(TypeError):
            Sq = Square(1, 2, 2.4, 1.3)
        with self.assertRaises(TypeError):
            Sw = Square(True, False)
        with self.assertRaises(TypeError):
            Sq = Square(1, 2, True, False)
        with self.assertRaises(TypeError):
            Sq = Square([1, 1], 2, 3, 4)
        with self.assertRaises(TypeError):
            Sq = Square((1, 2), 'a value', 'b value')
        with self.assertRaises(TypeError):
            Sq = Square({1: 3, 2: 4}, 5, 6)

    def test_area(self):
        """checks for area method"""
        Sq = Square(10, 10)
        self.assertEqual(Sq.area(), 100)
        with self.assertRaises(TypeError):
            AR = Sq.area(1)

    def test_str(self):
        """checks for __str__ method"""
        Sq = Square(1, 2, 3, 4)
        self.assertEqual("[Square] (4) 2/3 - 1", str(Sq))

    def test_update_args(self):
        """checks for update method: args"""
        Sq = Square(1, 2, 3, 4)
        Sq.update(6)
        self.assertEqual(6, Sq.id)
        Sq.update(6, 7)
        self.assertEqual(7, Sq.size)
        Sq.update(6, 7, 8)
        self.assertEqual(8, Sq.a)
        Sq.update(6, 7, 8, 9)
        self.assertEqual(9, Sq.b)

    def test_display(self):
        """checks display method"""
        Sq = Square(2, 0, 0, 4)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            Sq.display()
            output = bufferIO.getvalue()
            self.assertEqual(output, ('#' * 2 + '\n') * 2)
        Sq = Square(2, 3, 4, 5)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            Sq.display()
            output = bufferIO.getvalue()
            self.assertEqual(output,
                             ('\n' * 4 + (' ' * 3 + '#' * 2 + '\n') * 2))

    def test_update_kwargs(self):
        """checks for update method: kwargs"""
        Sq = Square(1, 2, 3, 4)
        Sq.update(6, id=7)
        self.assertEqual([Sq.id, Sq.size, Sq.a, Sq.b], [6, 1, 2, 3])
        Sq.update(6, 7, a=9, b=10)
        self.assertEqual([Sq.id, Sq.size, Sq.q, Sq.b], [6, 7, 2, 3])
        Sq.update(width=7, id=6, height=8)
        self.assertEqual([Sq.id, Sq.size, Sq.a, Sq.b], [6, 7, 2, 3])
        Sq.update(a=40, b=5)
        self.assertEqual([Sq.id, Sq.size, Sq.a, Sq.b], [6, 7, 40, 5])

    def test_dictionary(self):
        """checks for dictionary method"""
        Sq = Square(100, 300, 400, 500)
        Sq_dict = Sq.to_dictionary()
        self.assertEqual(Sq_dict['size'], 100)
        self.assertEqual(Sq_dict['a'], 300)
        self.assertEqual(Sq_dict['b'], 400)
        self.assertEqual(Sq_dict['id'], 500)


class TestSquare(unittest.TestCase):
    """checks class for Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_10_0(self):
        """checks Square class: check for attributes."""

        sq0 = Square(1)
        self.assertEqual(sq0.id, 1)
        sq1 = Square(5, 3, 4)
        self.assertEqual(sq1.height, 5)
        self.assertEqual(sq1.width, 5)
        self.assertEqual(sq1.a, 3)
        self.assertEqual(sq1.b, 4)
        self.assertEqual(sq1.id, 2)

    def test_10_1(self):
        """checks __str__ representation."""

        sq1 = Square(9, 4, 5, 6)
        self.assertEqual(str(sq1), "[Square] (6) 4/5 - 9")

    def test_10_2(self):
        """checks class square: check for inheritance."""

        sq1 = Square(6)
        self.assertTrue(isinstance(sq1, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(sq1, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    # def test_10_3(self):
    #     """checks class square check for missing args."""

    #     with self.assertRaises(TypeError) as a:
    #         sq1 = Square()
    #     self.assertEqual(
    #         "__init__() missing 1 required positional argument: 'size'", str(
    #             a.exception))

   def test_10_4(self):
        """checks square for methods inherited from Rectangle."""

        sq1 = Square(9)
        self.assertEqual(sq1.area(), 81)
        sq2 = Square(4, 1, 2, 5)
        sw2.update(7)
        self.assertEqual(sq2.id, 7)
        f = io.StringIO()
        sq3 = Square(4)
        with contextlib.redirect_stdout(f):
            sq3.display()
        sq = f.getvalue()
        res = "####\n####\n####\n####\n"
        self.assertEqual(sw, res)

    def test_11_0(self):
        """checks square class: check for size attribute."""

        sq1 = Square(8)
        self.assertEqual(sq1.size, 8)
        sq2 = Square(9, 8, 7, 2)
        self.assertEqual(sq2.size, 9)

    def test_11_1(self):
        """checks square class: check for wrong attributes."""

        with self.assertRaises(TypeError) as a:
            sq = Square("Elias", 2)
        self.assertEqual("width is always an integer", str(a.exception))
        with self.assertRaises(TypeError) as a:
            sq = Square(2, "Joy")
        self.assertEqual("a is always an integer", str(a.exception))
        with self.assertRaises(TypeError) as a:
            sq = Square(1, 2, "Foo", 3)
        self.assertEqual("b is always an integer", str(a.exception))
        with self.assertRaises(ValueError) as a:
            sq = Square(0, 2)
        self.assertEqual("width is always > 0", str(a.exception))
        with self.assertRaises(ValueError) as a:
            sq = Square(-1)
        self.assertEqual("width is always > 0", str(a.exception))
        with self.assertRaises(ValueError) as a:
            sq = Square(2, -3)
        self.assertEqual("a is always >= 0", str(a.exception))
        with self.assertRaises(ValueError) as a:
            sq = Square(2, 5, -5, 6)
        self.assertEqual("b is always >= 0", str(a.exception))

    def test_12_0(self):
        """checks update method on Square."""

        sq1 = Square(5)
        sq1.update(10)
        self.assertEqual(sq1.id, 10)
        sq1.update(a=12)
        self.assertEqual(sq1.a, 12)
        sq1.update(size=7, id=89, b=1)
        self.assertEqual(sq1.size, 7)
        self.assertEqual(sw1.id, 89)
        self.assertEqual(sq1.b, 1)
        sq1.update()
        self.assertEqual(sq1.size, 7)
        self.assertEqual(sw1.id, 89)
        self.assertEqual(sq1.b, 1)

    def test_12_1(self):
        """checks for update method on Square with wrong types."""

        sq1 = Square(9)
        with self.assertRaises(TypeError) as a:
            sq1.update(2, 3, 4, "elias")
        self.assertEqual("b is always an integer", str(a.exception))
        with self.assertRaises(TypeError) as a:
            sq1.update("elias", 8, 9)
        self.assertEqual("id is always an integer", str(a.exception))

    def test_14_0(self):
        """checks for public method to_dictionary."""

        sq1 = Square(10, 2, 1)
        sq1_dictionary = sq1.to_dictionary()
        sq_dictionary = {'a': 2, 'b': 1, 'id': 1, 'size': 10}
        self.assertEqual(len(sq1_dictionary), len(sq_dictionary))
        self.assertEqual(type(sq1_dictionary), dict)
        sq2 = Square(1, 1)
        sq2.update(**sq1_dictionary)
        sq2_dictionary = sq2.to_dictionary()
        self.assertEqual(len(sq1_dictionary), len(sq2_dictionary))
        self.assertEqual(type(sq2_dictionary), dict)
        self.assertFalse(sq1 == sq2)

    # def test_14_1(self):
    #     """checksfor public method to_dictionary with wrong args."""

    #     sq = "to_dictionary() takes 1 positional argument but 2 were given"
    #     with self.assertRaises(TypeError) as a:
    #         sq1 = Square(10, 2, 1, 9)
    #         sq1_dictionary = s1.to_dictionary("Hi")
    #     self.assertEqual(sq, str(a.exception))


if __name__ == '__main__':
    unittest.main()
