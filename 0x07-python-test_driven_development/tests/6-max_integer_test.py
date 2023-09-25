import unittest
max_integer = __import__('6-max_integer').max_integer

class MaxIntegerTestCase(unittest.TestCase):
    def test_ordered_list(self):
	ordered = [1, 2, 3, 4, 5, 6, 7]
	self.assertEqual(max_integer(ordered), 7)

    def test_unordered_list(self):
        unordered = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(max_integer(unordered), 7)

    def test_max_integer(self):
        # Test case 1: List with positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test case 2: List with negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test case 3: List with a mix of positive and negative integers
        self.assertEqual(max_integer([-5, 0, 10, -2]), 10)

        # Test case 4: List with duplicate integers
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

        # Test case 5: List with a single integer
        self.assertEqual(max_integer([8]), 8)

        # Test case 6: Empty list
        self.assertIsNone(max_integer([]))

        # Test case 7: List with floating-point numbers
        self.assertEqual(max_integer([1.5, 2.7, 3.2]), 3.2)

        # Test case 8: List with strings
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

        # Test case 9: List with a mix of different types
        self.assertEqual(max_integer([1, 'a', 2.5, True]), 2.5)

if __name__ == '__main__':
    unittest.main()
