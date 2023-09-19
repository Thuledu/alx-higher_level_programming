#!/usr/bin/python3

import sys
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle

from parameterized import parameterized

class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_instantiation_with_valid_arguments(self):
        valid_arguments = [
            (10, 2),
            (2, 10),
            (2, 2, 4),
            (4, 4, 2),
            (1, 2, 3, 4),
            (4, 3, 2, 1),
            (10, 2, 0, 0, 7)
        ]
        for args in valid_arguments:
            with self.subTest(args=args):
                r = Rectangle(*args)
                self.assertIsInstance(r, Base)

    def test_rectangle_instantiation_with_invalid_arguments(self):
        invalid_arguments = [
            (),
            (1,),
            (1, 2, 3, 4, 5, 6)
        ]
        for args in invalid_arguments:
            with self.subTest(args=args):
                with self.assertRaises(TypeError):
                    Rectangle(*args)

    def test_private_attributes(self):
        r = Rectangle(5, 5, 0, 0, 1)
        private_attributes = [
            ('__height', 5),
            ('__width', 5),
            ('__x', 0),
            ('__y', 0)
        ]
        for attr, value in private_attributes:
            with self.subTest(attr=attr):
                with self.assertRaises(AttributeError):
                    getattr(r, attr)

    def test_getters_and_setters(self):
        r = Rectangle(5, 7, 7, 5, 1)
        attributes = [
            ('height', 10),
            ('width', 10),
            ('x', 10),
            ('y', 10)
        ]
        for attr, value in attributes:
            with self.subTest(attr=attr):
                setattr(r, attr, value)
                self.assertEqual(getattr(r, attr), value)

class Rectangle:
    def __init__(self, *args):
        pass

class Base:
    pass


if __name__ == "__main__":
    unittest.main()
