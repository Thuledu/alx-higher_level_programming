import unittest
max_integer = __import__('6-max_integer').max_integer

def test_ordered_list(self):
	ordered = [1, 2, 3, 4, 5, 6, 7]
	self.assertEqual(max_integer(ordered), 7)

def test_unordered_list(self):
        unordered = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(max_integer(unordered), 7)
