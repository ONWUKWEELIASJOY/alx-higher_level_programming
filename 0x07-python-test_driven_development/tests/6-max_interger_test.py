#!/usr/bin/python3
import unittest
from 6-max_integer import max_integer

class MaxIntegerTestCase(unittest.TestCase):
    def test_positive_numbers(self):
        # Test case with positive numbers
        numbers = [1, 2, 3, 4, 5]
        result = max_integer(numbers)
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        # Test case with negative numbers
        numbers = [-1, -2, -3, -4, -5]
        result = max_integer(numbers)
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        # Test case with mixed positive and negative numbers
        numbers = [-1, 2, -3, 4, -5]
        result = max_integer(numbers)
        self.assertEqual(result, 4)

    def test_empty_list(self):
        # Test case with an empty list
        numbers = []
        result = max_integer(numbers)
        self.assertIsNone(result)

    def test_single_element_list(self):
        # Test case with a list containing a single element
        numbers = [3]
        result = max_integer(numbers)
        self.assertEqual(result, 3)

    def test_duplicate_max_numbers(self):
        # Test case with duplicate maximum numbers
        numbers = [1, 5, 3, 5, 2, 5]
        result = max_integer(numbers)
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()

