#!/usr/bin/python3
"""a cagar"""


import unittest
import io
import contextlib
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """a cagar"""
    def test_SquareinheritancefromBase(self):
        """a cagar"""
        Square.reset_objects()
        self.assertEqual(issubclass(Square, Base), True)

    def test_SquareinheritancefromRectangle(self):
        """a cagar"""
        Square.reset_objects()
        self.assertEqual(issubclass(Square, Rectangle), True)

    def test_objectinheritance(self):
        """a cagar"""
        Square.reset_objects()
        s1 = Square(5)
        self.assertEqual(isinstance(s1, Square), True)

    def test_errorfornoarguments(self):
        """a cagar"""
        Square.reset_objects()
        with self.assertRaises(TypeError) as e:
            s1 = Square()
        self.assertEqual(
            str(e.exception),
            "__init__() missing 1 required positional argument: 'size'")

    def test_errorfortoomanyarguments(self):
        """a cagar"""
        Square.reset_objects()
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 2, 3, 4, 5)
        self.assertEqual(
            str(e.exception),
            "__init__() takes from 2 to 5 positional" +
            " arguments but 6 were given")

    def test_negativesize(self):
        """a cagar"""
        Square.reset_objects()
        with self.assertRaises(ValueError) as e:
            s1 = Square(-1)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_negativexvalue(self):
        """a cagar"""
        Square.reset_objects()
        with self.assertRaises(ValueError) as e:
            s1 = Square(1, -2)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_negativeyvalue(self):
        """a cagar"""
        Square.reset_objects()
        with self.assertRaises(ValueError) as e:
            s1 = Square(1, 2, -2)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_0size(self):
        """a cagar"""
        Square.reset_objects()
        with self.assertRaises(ValueError) as e:
            s1 = Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_singlesquarecreation(self):
        """a cagar"""
        Square.reset_objects()
        s1 = Square(10)
        self.assertEqual(s1.id, 1)

    def test_multiplesquarecreation(self):
        """a cagar"""
        Square.reset_objects()
        s1 = Square(10)
        s2 = Square(2)
        s3 = Square(3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 3)

    def test_singlesquarecreationwithallvalues(self):
        """a cagar"""
        Square.reset_objects()
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)
        self.assertEqual(s1.id, 10)
        s2 = Square(10, 10, 10, 10)
        self.assertEqual(s2.width, 10)
        self.assertEqual(s2.height, 10)
        self.assertEqual(s2.x, 10)
        self.assertEqual(s2.y, 10)
        self.assertEqual(s2.id, 10)

    def test_multiplesquarecreationwithallvalues(self):
        """a cagar"""
        Square.reset_objects()
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)
        self.assertEqual(s1.id, 10)

    def test_badsizevaluewithstring(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square("foo", 1, 2, 3)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badxvaluewithstring(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, "foo", 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithstring(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, "foo", 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badyvaluewithsets(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, {1, 2, 3}, 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badsizevaluedicts(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square({"foo": 1}, 1, 2, 3)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badxvaluewithdicts(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, {"foo": 1}, 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithdicts(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, {"foo": 1}, 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badsizevaluefuncs(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(print(), 1, 2, 3)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badxvaluewithfuncs(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, print(), 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithfuncs(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, print(), 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_NaNsize(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(float('nan'), 10, 5, 7)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_NaNx(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(10, float('nan'), 5, 7)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_NaNy(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(10, 10, float('nan'), 7)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_sizesetterwithfunc(self):
        """a cagar"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, 2, 3)
            self.assertEqual(r1.size, 1)
            r1.size = print()
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_kwargsskipped(self):
        """a cagar"""
        Rectangle.reset_objects()
        s1 = Square(10, 10, 10, 10)
        s1.update(1, 2, 3, 4, id=10)
        self.assertEqual(s1.id, 1)

    def test_to_dict(self):
        """a cagar"""
        Square.reset_objects()
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'x': 2, 'size': 10, 'y': 1})

    def test_display__method(self):
        """a cagar"""
        Rectangle.reset_objects()
        s1 = Square(5)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s1.display()
        self.assertEqual(f.getvalue(), "#####\n#####\n#####\n#####\n#####\n")

    def test_display__method2(self):
        """a cagar"""
        Rectangle.reset_objects()
        s2 = Square(2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s2.display()
        self.assertEqual(f.getvalue(), "  ##\n  ##\n")
