#!/usr/bin/python3

import io
import sys
import os
import unittest
from models.base import Base
from models.square import Square


import unittest

class TestSquareInstantiation(unittest.TestCase):
    def setUp(self):
        self.square = Square(10, 2, 3, 4)

    def test_instantiation_with_valid_arguments(self):
        self.assertIsInstance(Square(10), Base)
        self.assertIsInstance(Square(10), Square)

    def test_instantiation_with_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_instantiation_with_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_instantiation_with_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_instantiation_with_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_instantiation_with_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_instantiation_with_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(self.square.__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        self.square.size = 8
        self.assertEqual(8, self.square.size)

    def test_width_getter(self):
        self.square.size = 8
        self.assertEqual(8, self.square.width)

    def test_height_getter(self):
        self.square.size = 8
        self.assertEqual(8, self.square.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)


if __name__ == "__main__":
    unittest.main()
