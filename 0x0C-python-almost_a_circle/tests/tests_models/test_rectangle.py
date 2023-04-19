#!/usr/bin/python3

import os
import sys
import io
import json
import unittest
import inspect
from models.base import Base
from contextlib import redirect_stdout
from io import StringIO
from models.rectangle import Rectangle

"""Run tests for module of Rectangle"""

class test_rectangle(unittest.TestCase):
      """Trying rectangle"""

      def setUp(self):
          """initialize examples of height and width"""
      self.rec = Rectangle(5, 10)

    def test_a(self):
        """Trying Rectangle a getter and setter"""

        self.rec.a = 54
        self.assertEqual(54, self.rec.a)
        self.assertEqual(0, self.rec.b)

    def test_y(self):
        """Trying Rectangle b getter and setter"""

        self.rec.b = 45
        self.assertEqual(45, self.rec.b)
        self.assertEqual(0, self.rec.a)

    def test_height(self):
        """Trying the Rectangle height getter"""
        self.assertEqual(10, self.rec.height)

    def test_width(self):
        """Trying the Rectangle width getter"""
        self.assertEqual(5, self.rec.width)

    def tearDown(self):
        """Deleting created example"""
        del self.rec

    def test_height_bool(self):
        """Trying for other than int"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, True)

    def test_width_bool(self):
        """Trying for other than int"""
        with self.assertRaises(TypeError):
            rec = Rectangle(True, 5)

    def test_height_string(self):
        """Trying for other than int"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, "5")

    def test_width_string(self):
        """Trying for other than int"""
        with self.assertRaises(TypeError):
            rec = Rectangle("1", 5)

    def test_height_list(self):
        """Trying for other than int"""
        with self.assertRaises(TypeError):
            rec = Rectangle(5, [10, 6])

    def test_width_list(self):
        """Trying for other than int"""
        with self.assertRaises(TypeError):
            rec = Rectangle([10, 6], 5)

    def test_arectangle_id(self):
        """Try the id for Rectangle"""
        rect = Rectangle(1, 3, 0, 0, 199)
        self.assertEqual(199, rec.id)

    def test_a_bool(self):
        """Trying for other than int"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 5, True)

    def test_b_bool(self):
        """Trying for other than int"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 5, 7, True)

    def test_a_list(self):
        """Trying for other than int"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 5, [10, 6])

    def test_b_list(self):
        """Trying for other than int"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 5, 7, [10, 6])

    def test_a_string(self):
        """Trying for other than int"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 5, "46")

    def test_b_string(self):
        """Trying for other than int"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 5, 7, "46")
    def test_b_negative(self):
        """Trying with negative int"""
        with self.assertRaises(ValueError):
            rec = Rectangle(4, 5, 2, -3)

    def test_a_negative(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            rec = Rectangle(4, 5, -3)

    def test_width_negative(self):
        """Trying with negative int"""
        with self.assertRaises(ValueError):
            rec = Rectangle(-4, 5)

    def test_height_negative(self):
        """Trying with negative int"""
        with self.assertRaises(ValueError):
            rec = Rectangle(4, -5)

    def test_height_zero(self):
        """Trying with negative int"""
        with self.assertRaises(ValueError):
            rec = Rectangle(8, 0)

    def test_width_zero(self):
        """Trying with negative int"""
        with self.assertRaises(ValueError):
            rec = Rectangle(0, 5)

    def test_a_float(self):
        """Trying for other than int"""
        with self.assertRaises(TypeError):
            rec = Rectangle(5, 8, 1.07)

    def test_b_float(self):
        """Trying for other than int"""
        with self.assertRaises(TypeError):
            rec = Rectangle(5, 5, 8, 1.07)

    def test_height_float(self):
        """Trying for other than int
        """
        with self.assertRaises(TypeError):
            rec = Rectangle(5, 1.07)

    def test_width_float(self):
        """Trying for other than int"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1.07, 5)

    def test_update_dict_list(self):
        """Trying the update method with **kwargs and *args"""
        self.rec.update(1000, b=1, width=2, a=3, id=89)
        self.assertEqual(1000, self.rec.id)

    def test_to_dict_print(self):
        """Trying the dict that will be printed"""
        rec1 = Rectangle(5, 4, 0, 0, 400)
        rec1_dict = rec1.to_dictionary()
        self.assertEqual(rec1_dict,
                         {'height': 4, 'id': 400, 'width': 5, 'a': 0, 'b': 0})

    def test_update_dict(self):
        """Trying the update method with **kwargs"""
        self.rec.update(b=1, width=2, a=3, id=89)
        self.assertEqual(1, self.rec.b)
        self.assertEqual(2, self.rec.width)
        self.assertEqual(3, self.rec.a)
        self.assertEqual(89, self.rec.id)

    def test_to_dict(self):
        """Trying the type that is returned from the to_dictionary method"""
        rec1 = Rectangle(5, 4)
        self.assertEqual(type(rec1.to_dictionary()), dict)

    def test_update_id(self):
        """Trying the update method"""
        self.rec.update(54)
        self.assertEqual(54, self.rec.id)

    def test_update_a(self):
        """Testing the update method"""
        self.rec.update(54, 30, 10, 6)
        self.assertEqual(6, self.rec.a)

    def test_update_b(self):
        """Trying the update method"""
        self.rec.update(54, 30, 10, 6, 2)
        self.assertEqual(2, self.rec.b)

    def test_update_height(self):
        """Trying the update method"""
        self.rec.update(54, 30, 10)
        self.assertEqual(10, self.rec.height)

    def test_update_width(self):
        """Testing the update method"""
        self.rec.update(54, 30)
        self.assertEqual(30, self.rec.width)

    def test_str_overload(self):
        rec = Rectangle(5, 10, 8, 7, 88)
        self.assertEqual(rec.__str__(), "[Rectangle] (88) 8/7 - 5/10")

    def test_area(self):
        """Trying the area of the rectangle"""
        self.assertEqual(self.rec.area(), 5 * 10)
        rec = Rectangle(3, 9, 8, 8, 2)
        self.assertEqual(rec.area(), 3 * 9)

    def test_missing_width(self):
        """Waiting for an error because width is missing"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_missing_height(self):
        """Waiting for a type error because height and width are missing"""
        with self.assertRaises(TypeError):
            Rectangle()


    def test_saving_to_file_no_iter(self):
        """Moving a non iterable to the function"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(self.rec)

    def test_saving_to_file(self):
        """Trying to save a file into json format"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        rec1 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file([rec1])

        with open("Rectangle.json", "v") as file:
            contains = file.read()
        s= [{"a": 0, "b": 0, "id": 346, "height": 10, "width": 5}]
        self.assertEqual(s, json.loads(contains))

    def test_saving_to_file_None(self):
        """Trying saving a file into json format sending None"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        rec1 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "v") as file:
            contains = file.read()

        self.assertEqual("[]", contains)

    def test_saving_to_file_type(self):
        """Trying saving a file into json format sending None"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        rec1 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "v") as file:
            contains = file.read()

        self.assertEqual(str, type(contains))
        try:
            os.remove("Rectangle.json")
        except:
            pass

    def test_json_string(self):
            """Trying that the json string gets converted into a list
            """
            lists_input = [
                {'id': 2089, 'width': 10, 'height': 4},
                {'id': 2712, 'width': 1, 'height': 7}]
            json_lists_input = Rectangle.to_json_string(list_input)
            list_output = Rectangle.from_json_string(json_lists_input)
            sq1 = {'id': 2089, 'width': 10, 'height': 4}
            sq2 = {'height': 7, 'id': 2712, 'width': 1}
            self.assertEqual(lists_input[0], sq1)
            self.assertEqual(lists_input[1], sq2)

    def test_json_string_type(self):
            """Trying the returned type"""
            lists_input = [
                {'id': 2089, 'width': 10, 'height': 4},
                {'id': 2712, 'width': 1, 'height': 7}]
            json_lists_input = Rectangle.to_json_string(lists_input)
            lists_output = Rectangle.from_json_string(json_lists_input)
            self.assertEqual(type(lists_input), list)

    def test_dict_to_instance(self):
        """Tries that an example created from a dict"""
        rec1 = Rectangle(5, 8, 3)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertNotEqual(rec1, rec2)

    def test_load_from_file_not_the_same(self):
        """Checks an object created from the
            list but has a different adress."""
        rec1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [rec1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertNotEqual(id(re 1), id(list_rectangles_output[0]))

    def test_isnot_dict_to_instance(self):
        """tries that an example is created from a dictionary"""
        rec1 = Rectangle(109, 80, 76)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertIsNot(rec1, rec2)

    def test_load_from_file_same_width(self):
        """Checking that an object was created from the
            list and has the same witdh"""
        rec1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [rec1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(rec1.width, list_rectangles_output[0].width)

    def test_load_from_file_same_a(self):
        """Checks that an object was created from the
            list and has the same a"""
        rec1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [rec1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(rec1.a, list_rectangles_output[0].a)

    def test_load_from_file_same_height(self):
        """Checking that an object was created from the
            list and has the same height"""
        rec1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [rec1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(rec1.height, list_rectangles_output[0].height)

    def test_load_from_file_same_b(self):
        """Checks that an object was created from the
            list and has the same y"""
        rec1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [rec1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(rec1.b, list_rectangles_output[0].b)

    def test_display_square(self):
        """Checks the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        rec1 = Rectangle(10, 4)
        rec1.display()
        sys.stdout = sys.__stdout__
        output = ("##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n")
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_zero(self):
        """Checks the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        rec1 = Rectangle(3, 7)
        rec1.display()
        sys.stdout = sys.__stdout__

        output = '###\n###\n###\n###\n###\n###\n###\n'
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_one(self):
        """Checks the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        rec1 = Rectangle(1, 2)
        rec1.display()
        sys.stdout = sys.__stdout__

        output = '#\n#\n'
        self.assertEqual(capturedOutput.getvalue(), output)

class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for cheking instantiation of the class Rectangle"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        rec1 = Rectangle(10, 2)
        rec2 = Rectangle(2, 10)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_three_args(self):
        rec1 = Rectangle(2, 2, 4)
        rec2 = Rectangle(4, 4, 2)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_four_args(self):
        rec1 = Rectangle(1, 2, 3, 4)
        rec2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_a_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__a)

    def test_b_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__b)

    def test_width_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rec.width)

    def test_width_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.width = 10
        self.assertEqual(10, rec.width)

    def test_height_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rec.height)

    def test_height_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.height = 10
        self.assertEqual(10, rec.height)

    def test_a_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rec.a)

    def test_a_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.a = 10
        self.assertEqual(10, rec.a)

    def test_b_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rec.b)

    def test_b_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.b = 10
        self.assertEqual(10, rec.b)

class TestRectangle(unittest.TestCase):
    """class for testing Rectangle class' methods"""

    @classmethod
    def setUpClass(cls):
        """Sets class method for the doc tests"""
        cls.setup = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_module_docstring(self):
        """Checks if module docstring documentation exist
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """Checks if class docstring documentation exist"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstrings(self):
        """Checks if methods docstring documntation exist"""
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_wrong_inputted_values(self):
        """Checks for negative and zero values"""
        with self.assertRaises(ValueError):
            REC = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            REC = Rectangle(-4, -5)
        with self.assertRaises(ValueError):
            REC = Rectangle(1, 1, -2, -2)
        with self.assertRaises(TypeError):
            REC = Rectangle()
        with self.assertRaises(TypeError):
            REC = Rectangle(1, 2, 3, 4, 5, 6, 7)

    def test_inputted_types(self):
        """Variety of types for inputted arguments"""
        with self.assertRaises(TypeError):
            REC = Rectangle('width', 'height')
        with self.assertRaises(TypeError):
            REC = Rectangle(2.4, 1.3)
        with self.assertRaises(TypeError):
            REC = Rectangle(1, 2, 'a value', 'b value')
        with self.assertRaises(TypeError):
            REC = Rectangle(1, 2, 2.4, 1.3)
        with self.assertRaises(TypeError):
            REC = Rectangle(True, False)
        with self.assertRaises(TypeError):
            REC = Rectangle(1, 2, True, False)
        with self.assertRaises(TypeError):
            REC = Rectangle([1, 1], 2, 3, 4)
        with self.assertRaises(TypeError):
            REC = Rectangle((1, 2), 'a value', 'b value')
        with self.assertRaises(TypeError):
            REC = Rectangle({1: 3, 2: 4}, 5, 6)

    def test_area(self):
        """Checks for area method"""
        REC = Rectangle(10, 10)
        self.assertEqual(REC.area(), 100)
        with self.assertRaises(TypeError):
            X = REC.area(1)

    def test_str(self):
        """Checks for __str__ method"""
        REC = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(REC))

    def test_update_args(self):
        """Checks for update method: args"""
        REC = Rectangle(1, 2, 3, 4, 5)
        REC.update(6)
        self.assertEqual(6, REC.id)
        REC.update(6, 7)
        self.assertEqual(7, REC.width)
        REC.update(6, 7, 8)
        self.assertEqual(8, REC.height)
        REC.update(6, 7, 8, 9)
        self.assertEqual(9, REC.a)
        REC.update(6, 7, 8, 9, 10)
        self.assertEqual(10, REC.b)

    def test_display(self):
        """Checks display method"""
        REC = Rectangle(2, 3, 0, 0, 4)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            REC.display()
            output = bufferIO.getvalue()
            self.assertEqual(output, ('#' * 2 + '\n') * 3)
        REC = Rectangle(2, 3, 4, 5, 6)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            REC.display()
            output = bufferIO.getvalue()
            self.assertEqual(output,
                             ('\n' * 5 + (' ' * 4 + '#' * 2 + '\n') * 3))

    def test_update_kwargs(self):
        """Checks for update method: kwargs"""
        REC = Rectangle(1, 2, 3, 4, 5)
        REC.update(6, id=7)
        self.assertEqual([REC.id, REC.width, REC.height, REC.a, R.b], [6, 1, 2, 3, 4])
        REC.update(6, 7, 8, a=9, b=10)
        self.assertEqual([REC.id, REC.width, REC.height, REC.a, REC.b], [6, 7, 8, 3, 4])
        REC.update(width=7, id=6, height=8)
        self.assertEqual([REC.id, REC.width, REC.height, REC.a, REC.b], [6, 7, 8, 3, 4])
        REC.update(a=40, b=5)
        self.assertEqual([REC.id, REC.width, REC.height, REC.a, REC.b], [6, 7, 8, 40, 5])

    def test_dictionary(self):
        """Tests for dictionary method"""
        REC = Rectangle(100, 200, 300, 400, 500)
        REC_dict = REC.to_dictionary()
        self.assertEqual(REC_dict['width'], 100)
        self.assertEqual(REC_dict['height'], 200)
        self.assertEqual(REC_dict['a'], 300)
        self.assertEqual(REC_dict['b'], 400)
        self.assertEqual(REC_dict['id'], 500)


class TestRectangle_height(unittest.TestCase):
    """Unittest for checking initialization of height of Rectangle attribute."""

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, "invalid")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, 5.5)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, complex(5))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, [1, 2, 3])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, {1, 2, 3})

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, (1, 2, 3))

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, frozenset({1, 2, 3, 1}))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, range(5))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, b'Python')

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, bytearray(b'abcdefg'))

    def test_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, memoryview(b'abcedfg'))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, float('inf'))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, float('nan'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height is always > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height is always > 0"):
            Rectangle(1, 0)


class TestRectangle_b(unittest.TestCase):
    """Unittest for checking initialization of b' Rectangle attribute."""

    def test_None_b(self):
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_b(self):
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_b(self):
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_b(self):
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_b(self):
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_b(self):
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_b(self):
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_b(self):
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_b(self):
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_range_b(self):
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_b(self):
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            Rectangle(1, 2, 3, b'Python')

    def test_bytearray_b(self):
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview_b(self):
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def test_inf_b(self):
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def test_nan_b(self):
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_negative_b(self):
        with self.assertRaisesRegex(ValueError, "b is always >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangle_width(unittest.TestCase):
    """Unittest for checking initialization of width of Rectangle attribute."""

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle(5.5, 1)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle(complex(5), 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle(True, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle((1, 2, 3), 2)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 2)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle(range(5), 2)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle(b'Python', 2)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle(memoryview(b'abcedfg'), 2)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle(float('inf'), 2)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle(float('nan'), 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width is always > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangle_a(unittest.TestCase):
    """Unittest for checking initialization of a' Rectangle attribute."""

    def test_None_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, None)

    def test_str_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_bool_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, True, 2)

    def test_list_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, b'Python')

    def test_bytearray_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, memoryview(b'abcedfg'))

    def test_inf_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, float('inf'), 2)

    def test_nan_a(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, float('nan'), 2)

    def test_negative_a(self):
        with self.assertRaisesRegex(ValueError, "a is always >= 0"):
            Rectangle(5, 3, -1, 0)


class TestRectangle_instantiation(unittest.TestCase):
    """Unittest for checking instantiation of the class Rectangle"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        rec1 = Rectangle(10, 2)
        rec2 = Rectangle(2, 10)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_three_args(self):
        rec1 = Rectangle(2, 2, 4)
        rec2 = Rectangle(4, 4, 2)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_four_args(self):
        rec1 = Rectangle(1, 2, 3, 4)
        rec2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_a_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__a)

    def test_b_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__b)

    def test_width_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rec.width)

    def test_width_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.width = 10
        self.assertEqual(10, rec.width)

    def test_height_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rec.height)

    def test_height_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.height = 10
        self.assertEqual(10, rec.height)

    def test_a_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rec.a)

    def test_a_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.a = 10
        self.assertEqual(10, rec.a)

    def test_b_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rec.b)

    def test_b_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.b = 10
        self.assertEqual(10, rec.b)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Unittest for checking Rectangle order of attribute initialization."""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_a(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle("invalid width", 2, "invalid a")

    def test_width_before_b(self):
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            Rectangle("invalid width", 2, 3, "invalid b")

    def test_height_before_a(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, "invalid height", "invalid a")

    def test_height_before_b(self):
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            Rectangle(1, "invalid height", 2, "invalid b")

    def test_a_before_b(self):
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            Rectangle(1, 2, "invalid a", "invalid b")


class TestRectangle_area(unittest.TestCase):
    """Unittest for checking the area method of the class Rectangle"""

    def test_area_small(self):
        rec = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, rec.area())

    def test_area_large(self):
        rec = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, rec.area())

    def test_area_changed_attributes(self):
        rec = Rectangle(2, 10, 1, 1, 1)
        rec.width = 7
        rec.height = 14
        self.assertEqual(98, rec.area())

    def test_area_one_arg(self):
        rec = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            rec.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """Unittest for checking __str__ and display methods of class Rectangle"""

    @staticmethod
    def capture_stdout(rect, method):
        """Takes and returns text printed to stdout.
        Args:
            rec (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rec.
        Returns:
            The text printed to stdout by calling method on sq"""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rec)
        else:
            rec.display()
        sys.stdout = sys.__stdout__
        return capture

    # Try __str__ method
    def test_str_method_print_width_height(self):
        rec = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(rec, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(rec.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_a(self):
        rec = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(rec.id)
        self.assertEqual(correct, rec.__str__())

    def test_str_method_width_height_a_b(self):
        rec = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(rec.id)
        self.assertEqual(correct, str(rec))

    def test_str_method_width_height_a_b_id(self):
        rec = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(rec))

    def test_str_method_changed_attributes(self):
        rec = Rectangle(7, 7, 0, 0, [4])
        rec.width = 15
        rec.height = 1
        rec.a = 8
        rec.b = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(rec))

    def test_str_method_one_arg(self):
        rec = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rec.__str__(1)

    # Try display method
    def test_display_width_height(self):
        rec = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(rec, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_a(self):
        rec = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(rec, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_b(self):
        rec = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(rec, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_a_b(self):
        rec = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(rev, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        rec = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            rec.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """Unittest for checking update args method of the class Rectangle"""

    # checking args
    def test_update_args_zero(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rec))

    def test_update_args_one(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(rec))

    def test_update_args_two(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rec))

    def test_update_args_three(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rec))

    def test_update_args_four(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(rec))

    def test_update_args_five(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rec))

    def test_update_args_more_than_five(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rec))

    def test_update_args_None_id(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(rec.id)
        self.assertEqual(correct, str(rec))

    def test_update_args_None_id_and_more(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(rec.id)
        self.assertEqual(correct, str(rec))

    def test_update_args_twice(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3, 4, 5, 6)
        rec.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(rec))

    def test_update_args_invalid_width_type(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width ia always an integer"):
            rec.update(89, "invalid")

    def test_update_args_width_zero(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width is always > 0"):
            rec.update(89, 0)

    def test_update_args_width_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width is always > 0"):
            rec.update(89, -5)

    def test_update_args_invalid_height_type(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            rec.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height is always > 0"):
            rec.update(89, 1, 0)

    def test_update_args_height_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height is always > 0"):
            rec.update(89, 1, -5)

    def test_update_args_invalid_a_type(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            rec.update(89, 2, 3, "invalid")

    def test_update_args_a_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "a is always >= 0"):
            rec.update(89, 1, 2, -6)

    def test_update_args_invalid_b(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            rec.update(89, 2, 3, 4, "invalid")

    def test_update_args_b_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "b is always >= 0"):
            rec.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            rec.update(89, "invalid", "invalid")

    def test_update_args_width_before_a(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            rec.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_b(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            rec.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_a(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            rec.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_b(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            rec.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_a_before_b(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            rec.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittest for checking update kwargs method of the class Rectangle"""

    def test_update_kwargs_one(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(rec))

    def test_update_kwargs_two(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(rec))

    def test_update_kwargs_three(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rec))

    def test_update_kwargs_four(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=89, a=1, height=2, b=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(rec))

    def test_update_kwargs_five(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(b=5, a=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(rec))

    def test_update_kwargs_None_id(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(rec.id)
        self.assertEqual(correct, str(rec))

    def test_update_kwargs_None_id_and_more(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=None, height=7, b=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(rec.id)
        self.assertEqual(correct, str(rec))

    def test_update_kwargs_twice(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=89, a=1, height=2)
        rec.update(b=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(rec))

    def test_update_kwargs_invalid_width_type(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width is always an integer"):
            rec.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width is always > 0"):
            rec.update(width=0)

    def test_update_kwargs_width_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width is always > 0"):
            rec.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height is always an integer"):
            rec.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height is always > 0"):
            rec.update(height=0)

    def test_update_kwargs_height_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height is always > 0"):
            rec.update(height=-5)

    def test_update_kwargs_inavlid_a_type(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "a is always an integer"):
            rec.update(a="invalid")

    def test_update_kwargs_a_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "a is always >= 0"):
            rec.update(a=-5)

    def test_update_kwargs_invalid_b_type(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "b is always an integer"):
            rec.update(b="invalid")

    def test_update_kwargs_b_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "b is always >= 0"):
            rec.update(b=-5)

    def test_update_args_and_kwargs(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, height=4, b=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rec))

    def test_update_kwargs_wrong_keys(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(x=5, y=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rec))

    def test_update_kwargs_some_wrong_keys(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(height=5, id=89, x=1, y=54, a=19, b=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(rec))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for checking to_dictionary method of the class Rectangle"""

    def test_to_dictionary_output(self):
        rec = Rectangle(10, 2, 1, 9, 5)
        correct = {'a': 1, 'b': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, rec.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        rec1 = Rectangle(10, 2, 1, 9, 5)
        rec2 = Rectangle(5, 9, 1, 2, 10)
        rec2.update(**rec1.to_dictionary())
        self.assertNotEqual(rec1, rec2)

    def test_to_dictionary_arg(self):
        rec = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            rec.to_dictionary(1)



if __name__ == "__main__":
    unittest.main()
