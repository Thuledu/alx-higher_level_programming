#!/usr/bin/python3

import unittest
import os
from parameterized import parameterized
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_initialization(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_saving_id(self):
        base = Base(100)
        self.assertEqual(base.id, 100)

class TestBaseInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b_unique = Base(12)
        self.b_with_id = Base(12)

    def test_no_arg(self):
        self.assertEqual(self.b1.id, self.b2.id - 1)

    def test_three_bases(self):
        self.assertEqual(self.b1.id, self.b3.id - 2)

    def test_None_id(self):
        self.assertEqual(self.b1.id, self.b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(14, self.b_unique.id)

    def test_nb_instances_after_unique_id(self):
        self.assertEqual(self.b1.id, self.b3.id - 1)

    def test_id_public(self):
        self.b_with_id.id = 15
        self.assertEqual(15, self.b_with_id.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(14).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(6), Base(range(6)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcdefg'), Base(bytearray(b'abcdefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcdefg'), Base(memoryview(b'abcdefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('NaN'), Base(float('NaN')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    """Unit tests for the to_json_string method of the Base class."""

    @parameterized.expand([
        (Rectangle(10, 7, 2, 8, 6), 58),  # rectangle with one dictionary
        (Square(10, 2, 3, 4), 43)  # square with one dictionary
    ])
    def test_to_json_string_one_dict(self, shape, expected_length):
        self.assertEqual(expected_length, len(Base.to_json_string([shape.to_dictionary()])))

    @parameterized.expand([
        ([Rectangle(2, 3, 5, 19, 2).to_dictionary(), Rectangle(4, 2, 4, 1, 12).to_dictionary()], 116),
        ([Square(10, 2, 3, 4).to_dictionary(), Square(4, 5, 21, 2).to_dictionary()], 86)  
    ])
    def test_to_json_string_two_dicts(self, shapes, expected_length):
        self.assertEqual(expected_length, len(Base.to_json_string(shapes)))

    @parameterized.expand([
        ("[]", []),  # empty list
        ("[]", None)  # None input
    ])
    def test_to_json_string_empty_input(self, expected_output, input_value):
        self.assertEqual(expected_output, Base.to_json_string(input_value))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertIsInstance(Base.to_json_string([r.to_dictionary()]), str)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertIsInstance(Base.to_json_string([s.to_dictionary()]), str)



class TestBaseSaveToFile(unittest.TestCase):
    """Unit tests figured the save_to_file method of the Base class."""

    @classmethod
    def setUpClass(cls):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_shape(self):
        r = Rectangle(10, 17, 12, 18, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(53, len(f.read()))

    def test_save_to_file_two_shapes(self):
        r1 = Rectangle(10, 17, 12, 18, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(105, len(f.read()))

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 17, 12, 18)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertEqual(39, len(f.read()))

    @parameterized.expand([
        (Square(10, 17, 12, 18), 39),  # one square
        (Square(8, 1, 2, 3), 77)  # two squares
    ])
    def test_save_to_file_one_or_two_squares(self, shape, expected_length):
        Square.save_to_file([shape])
        with open("Square.json", "r") as f:
            self.assertEqual(expected_length, len(f.read()))

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 12)
        Square.save_to_file([s])
        s = Square(10, 17, 12, 18)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertEqual(39, len(f.read()))

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


if __name__ == "__main__":
    unittest.main()
