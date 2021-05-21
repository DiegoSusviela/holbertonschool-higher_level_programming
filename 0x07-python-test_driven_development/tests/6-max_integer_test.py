#!/usr/bin/python3
"""Unittest max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ tests for positive output"""
    def test_positiveoutput(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    """ tests for negative output"""
    def test_max_negativeoutput(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    """ tests for one number"""
    def test_max_onenumber(self):
        self.assertEqual(max_integer([3]), 3)
    """ tests for one negative number"""
    def test_max_onenegativenumber(self):
        self.assertEqual(max_integer([-1]), -1)
    """ tests for unordered list"""
    def test_max_unordered(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)
    """ tests for identical values"""
    def test_max_identicalvalues(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
    """ tests for strings"""
    def test_max_strings(self):
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
    """ tests for raising error when None is passed"""
    def test_max_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)
    """ tests for True"""
    def test_max_True(self):
        with self.assertRaises(TypeError):
            max_integer(True)
    """ tests for "list is empty" exists"""
    def test_emptylist(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
