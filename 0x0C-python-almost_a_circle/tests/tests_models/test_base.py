#!/usr/bin/python3


from models.square import Square
import inspect
from models.base import Base
import unittest
import inspect

"""Test cases base module"""

class test_base(unittest.TestCase):
    """Test base"""

    def test_id(self):
        """Using a valid id"""
        bs = Base(50)
        self.assertEqual(50, bs.id)

    def test_id_none(self):
        """Using no id"""
        bs = Base()
        self.assertEqual(1, bs.id)

    def test_id_list(self):
        """Using an id that is not an int"""
        bs = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], bs.id)

    def test_id_zero(self):
        """Using an id 0"""
        bs = Base(0)
        self.assertEqual(0, bs.id)

    def test_id_string(self):
        """Using an id that is not an int"""
        bs = Base("Betty")
        self.assertEqual("Betty", bs.id)

    def test_id_dict(self):
        """Using an id that is not an int"""
        bs = Base({"id": 109})
        self.assertEqual({"id": 109}, bs.id)

    def test_id_negative(self):
        """Using a negative id"""
        bs = Base(-20)
        self.assertEqual(-20, bs.id)

    def test_id_tuple(self):
        """Using an id that is not an int"""
        bs = Base((8,))
        self.assertEqual((8,), bs.id)

    def test_to_json_None(self):
        """Trying the json string"""
        sq = Square(1, 0, 0, 609)
        j_dict = sq.to_dictionary()
        j_string = Base.to_json_string(None)
        self.assertEqual(j_string, "[]")

    def test_to_json_type(self):
        """Trying the json string"""
        sq = Square(1)
        j_dict = sq.to_dictionary()
        j_string = Base.to_json_string([j_dict])
        self.assertEqual(type(j_string), str)

    def test_to_json_Empty(self):
        """Trying the json string"""
        sq = Square(1, 0, 0, 609)
        j_dict = sq.to_dictionary()
        j_string = Base.to_json_string([])
        self.assertEqual(j_string, "[]")

    def test_to_json_value(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        j_dict = sq.to_dictionary()
        j_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(j_string),
                         [{"id": 609, "b": 0, "size": 1, "a": 0}])

class TestSquare(unittest.TestCase):
    """class for Trying Base class method"""

    @classmethod
    def test_class_docstring(self):
        """Checks class docstring documentation existence"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def setUpClass(cls):
        """creates class method for the document test"""
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_func_docstrings(self):
        """Tests if methods docstring documntation exist"""
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_module_docstring(self):
        """Tests if module docstring documentation exist"""
        self.assertTrue(len(Base.__doc__) >= 1)
