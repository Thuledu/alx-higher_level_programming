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

class TestRectangleHeight(unittest.TestCase):
    """Test case for Rectangle height attribute."""

    def test_invalid_height(self):
        invalid_values = [
            None,
            "invalid",
            5.5,
            complex(5),
            {"a": 1, "b": 2},
            [1, 2, 3],
            {1, 2, 3},
            (1, 2, 3),
            frozenset({1, 2, 3, 1}),
            range(5),
            b'Python',
            bytearray(b'abcdefg'),
            memoryview(b'abcedfg'),
            float('inf'),
            float('nan')
        ]

        for value in invalid_values:
            with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(1, value)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangleWidth(unittest.TestCase):
    """Test case for Rectangle width attribute."""

    def test_invalid_width(self):
        invalid_values = [
            None,
            "invalid",
            5.5,
            complex(5),
            {"a": 1, "b": 2},
            True,
            [1, 2, 3],
            {1, 2, 3},
            (1, 2, 3),
            frozenset({1, 2, 3, 1}),
            range(5),
            b'Python',
            bytearray(b'abcdefg'),
            memoryview(b'abcedfg'),
            float('inf'),
            float('nan')
        ]

        for value in invalid_values:
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(value, 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangleX(unittest.TestCase):
    """Test case for Rectangle x attribute."""

    def test_invalid_x(self):
        invalid_values = [
            None,
            "invalid",
            5.5,
            complex(5),
            {"a": 1, "b": 2},
            True,
            [1, 2, 3],
            {1, 2, 3},
            (1, 2, 3),
            frozenset({1, 2, 3, 1}),
            range(5),
            b'Python',
            bytearray(b'abcdefg'),
            memoryview(b'abcedfg'),
            float('inf'),
            float('nan')
        ]

        for value in invalid_values:
            with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, value, 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)

class TestRectangleY(unittest.TestCase):
    """Test case for Rectangle y attribute."""

    def test_invalid_y(self):
        invalid_values = [
            None,
            "invalid",
            5.5,
            complex(5),
            {"a": 1, "b": 2},
            [1, 2, 3],
            {1, 2, 3},
            (1, 2, 3),
            frozenset({1, 2, 3, 1}),
            range(5),
            b'Python',
            bytearray(b'abcdefg'),
            memoryview(b'abcedfg'),
            float('inf'),
            float('nan')
        ]

        for value in invalid_values:
            with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, value)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangleOrderOfInitialization(unittest.TestCase):
    """Test case for checking the order of initialization."""

    def test_invalid_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "the width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")
    
    def test_invalid_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "the width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_invalid_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "the width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_invalid_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "the height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_invalid_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "the height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_invalid_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "the x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")

class TestRectangleStdout(unittest.TestCase):
    """Test case for testing __str__ and display method of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout."""
        capture = io.StringIO()
        sys.stdout = capture

        if method == "print":
            print(rect)
        else:
            rect.display()

        sys.stdout = sys.__stdout__
        return capture.getvalue()

    def test_str_method_width_height_x_y_id(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_width_height_x_y(self):
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x(self):
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_print_width_height(self):
        r = Rectangle(4, 6)
        capture = TestRectangleStdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture)

    def test_str_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangleStdout.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture)

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangleStdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture)

    def test_display_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangleStdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture)

    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangleStdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture)

    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)

class TestRectangleUpdateArgs(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(10, 10, 10, 10, 10)

    def test_update_args_id(self):
        self.rectangle.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(self.rectangle))

    def test_update_args_zero(self):
        self.rectangle.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(self.rectangle))

    def test_update_args_width_height(self):
        self.rectangle.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(self.rectangle))

    def test_update_args_width_height_x_y(self):
        self.rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(self.rectangle))

    def test_update_args_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.rectangle.update(89, 0)

    def test_update_args_invalid_width_type(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.rectangle.update(89, "invalid")

    def test_update_args_None_id(self):
        self.rectangle.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(self.rectangle.id)
        self.assertEqual(correct, str(self.rectangle))

    def test_update_args_None_id_and_more(self):
        self.rectangle.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(self.rectangle.id)
        self.assertEqual(correct, str(self.rectangle))

    def test_update_args_multiple_times(self):
        self.rectangle.update(89, 2, 3, 4, 5, 6)
        self.rectangle.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(self.rectangle))

class TestRectangleUpdateKwargs(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(10, 10, 10, 10, 10)

    def test_update_kwargs(self):
        test_cases = [
            {
                'kwargs': {'id': 1},
                'expected': "[Rectangle] (1) 10/10 - 10/10"
            },
            {
                'kwargs': {'width': 2, 'id': 1},
                'expected': "[Rectangle] (1) 10/10 - 2/10"
            },
            {
                'kwargs': {'width': 2, 'height': 3, 'id': 89},
                'expected': "[Rectangle] (89) 10/10 - 2/3"
            },
            {
                'kwargs': {'id': 89, 'x': 1, 'height': 2, 'y': 3, 'width': 4},
                'expected': "[Rectangle] (89) 1/3 - 4/2"
            },
            {
                'kwargs': {'y': 5, 'x': 8, 'id': 99, 'width': 1, 'height': 2},
                'expected': "[Rectangle] (99) 8/5 - 1/2"
            }
        ]

        for test_case in test_cases:
            self.rectangle.update(**test_case['kwargs'])
            self.assertEqual(test_case['expected'], str(self.rectangle))

    def test_update_kwargs_none_id(self):
        self.rectangle.update(id=None)
        expected = "[Rectangle] ({}) 10/10 - 10/10".format(self.rectangle.id)
        self.assertEqual(expected, str(self.rectangle))

    def test_update_kwargs_invalid_width_type(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.rectangle.update(width="invalid")

class TestRectangleToDictionary(unittest.TestCase):
    def test_to_dictionary_invalid_argument(self):
        rectangle = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            rectangle.to_dictionary(1)

    def test_to_dictionary_output(self):
        rectangle = Rectangle(10, 2, 1, 9, 5)
        expected = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertEqual(expected, rectangle.to_dictionary())

if __name__ == "__main__":
    unittest.main()
