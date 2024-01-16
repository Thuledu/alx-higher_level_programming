#!/usr/bin/python3

from unittest.mock import patch
import unittest
import json
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare_instantiation(unittest.TestCase):
     """ Defines tests for the Square class """

    def clearUp(self):
        """ Cleans up after each test """
        pass

    def test_base(self):
        self.assertIsInstance(Square(10), Base)

    def testing_args(self):
        """Testing multiple arguments"""
        s1 = Square(10, 2, 4, 8)
        s2 = Square(9, 2, 11, 3)
        self.assertEqual(s1.id, s2.id - 1)

    def test_width(self):
        """Testing Width"""
        s = Square(4, 2, 9, 8)
        s.size = 10
        self.assertEqual(10, s.width)

    def test_height(self):
        """Testing Height"""
        s = Square(4, 2, 9, 8)
        s.size = 10
        self.assertEqual(10, s.height)

    def test_load_json_file(self):
        """ Test load JSON file """
        load_file = Square.load_from_file()
        self.assertEqual(load_file, load_file)

