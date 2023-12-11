#!/usr/bin/python3

# test_base.py
import json
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseMethods(unittest.TestCase):
    """Defines tests for the Base class"""

    def clearUp(self):
        """Cleans up after each test"""
        pass

    def buildUp(self):
        """Runs for each test"""
        Base._Base__nb_objects = 0
        self.new_base = Base(id=1)

    def present_docstring(self):
        """Test if docstring is present"""
        self.assertIsNotNone(Base.__doc__)

    def checks_instance_variables_test(self):
        """Checks instance variables"""
        self.assertEqual(self.new_base.id, 1)

    def tests_random_ids(self):
        """Test random arguments passed"""
        test1 = Base(-7)
        self.assertEqual(test1.id, -7)
        test2 = Base()
        self.assertEqual(test2.id, 1)
        test3 = Base(333)
        self.assertEual(test3.id, 333)
        test4 = Base(43)
        self.assertEqual(test4.id, 43)

    def testing_to_json_string(self):
        """Test to_json_string method"""
        r1 = Rectangle(11, 1, 7, 4)
        r2 = Rectangle(10, 2, 8, 3)
        dict1 = r1.to_dictionary()
        dict2 = r2.to_dictionary()
        json_dict1 = [{"x": 4, "width": 11, "id": 1, "height": 7, "y": 1}]
        json_dict2 = [{"x": 2, "width": 10, "id": 1, "height": 8, "y": 3}]
        json_string = Base.to_json_string([dict1, dict2])
        self.assertNotEqual(dict1, json_dict1)
        self.assertNotEqual(dict2, json_dict2)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(type(dict1), dict)
        self.assertEqual(type(json_string), str)
        self.assertTrue(type(Base.to_json_string("[]")) is str)
        self.assertTrue(type(Base.to_json_string(None)) is str)
        self.assertTrue(type(json_string), str)
        d = json.loads(json_string)
        self.assertEqual(d, [dict1, dict2])

    def testing_from_json_string(self):
        """Test from_json_string method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        list_input = [{"x": 4, "width": 11, "id": 1, "height": 7, "y": 1}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        list_output2 = [{'x': 2, 'width': 10, 'id': 1, 'height': 8, 'y': 1}]
        self.assertEqual(list_output, list_output2)
        self.assertTrue(type(list_output), list)

    def test_constructor_signature(self):
        """Tests constructor signature"""
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)


