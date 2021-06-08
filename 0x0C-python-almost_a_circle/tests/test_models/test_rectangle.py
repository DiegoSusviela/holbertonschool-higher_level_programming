#!/usr/bin/python3
"""a cagar"""


import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import contextlib



class TestBaseClass(unittest.TestCase):
    """a cagar"""

    def test_Rectangleinheritance(self):
        """a cagar"""
        Rectangle.reset_objects()
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_objectinheritance(self):
        """a cagar"""
        Rectangle.reset_objects()
        r1 = Rectangle(1, 1)
        self.assertEqual(isinstance(r1, Rectangle), True)

    def test_errorfornoarguments(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle()
        self.assertEqual(
            str(e.exception),
            "__init__() missing 2 required positional arguments: 'width' and" +
            " 'height'")

    def test_kwargsskipped(self):
        """a cagar"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(1, 2, 3, 4, 5, id=10)
        self.assertEqual(r1.id, 1)

    def test_badkeyignored(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(1, 2, 3, 4, 5, foo=20)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_fornoargumentstoupdate(self):
        """a cagar"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update()
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

    def test_errorfortoomanyarguments(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, 3, 4, 5, 6)
        self.assertEqual(
            str(e.exception),
            "__init__() takes from 3 to 6 positional " +
            "arguments but 7 were given")
    def test_display__method(self):
        """a cagar"""
        Rectangle.reset_objects()
        r1 = Rectangle(2, 3, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_display__method2(self):
        """a cagar"""
        Rectangle.reset_objects()
        r2 = Rectangle(3, 2, 1, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r2.display()
        self.assertEqual(f.getvalue(), " ###\n ###\n")
