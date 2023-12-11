#!/usr/bin/python3

import io
import sys
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle_instantiation(unittest.TestCase):
    """ Defines tests for the Rectangle class """

    def test_rectangle_base(self):
        self.assertIsInstance(Rectangle(2, 10), Base)

    def clearUp(self):
        """ Cleans up after each test """
        pass

    def test_args(self):
        """Test two arguments"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_arg_passed(self):
        """ Test for passing one or no argument """
        with self.assertRaises(TypeError):
            Rectangle(20)
            Rectangle()

    def test_width(self):
        """Test Width"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 2, 8, 9, 1).__width)
            with self.assertRaises(TypeError, "width must be an integer"):
            Rectangle("Holland", 9)
            Rectangle("X", 8)
            Rectangle(True, 8)

    def test_height(self):
        """Test Height"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 2, 8, 9, 1).__height)
            Rectangle(True, 6)
        with self.assertRaises(TypeError, "x must be an integer"):
            Rectangle(5, 4, "YH")
            Rectangle(5, 4, "Y")
            Rectangle(True, 2, 4)
        with self.assertRaises(TypeError, "y must be an integer"):
            Rectangle(3, 2, 1, "Y" )
            Rectangle(3, 2, 1, "YH")
            Rectangle(True, 1, 2, 3)


