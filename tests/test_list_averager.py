"""Module tests for ListAverager class."""
import unittest
from list_averager import ListAverager


class TestListAverager(unittest.TestCase):
    """Class representing tests for ListAverager"""

    def setUp(self):
        self.averager = ListAverager()

    def test_list_average(self):
        """method checking return values of list_average"""
        self.assertEqual(self.averager.list_average([32, 5, 67, 8]), 28)
        self.assertEqual(self.averager.list_average([1, 2, 3, 4]), 2.5)

    def test_list_arg_type(self):
        """method checking exception raising TypeError if arg not list of numbers"""
        with self.assertRaises(TypeError):
            self.averager.list_average(3)
        with self.assertRaises(TypeError):
            self.averager.list_average(None)
        with self.assertRaises(TypeError):
            self.averager.list_average(['qwe', '123'])

    def test_comp_averages(self):
        """method checking return values of comp_averages"""
        self.assertEqual(self.averager.comp_averages([1, 2, 3, 4], [32, 5, 67, 8]), -1)
        self.assertEqual(self.averager.comp_averages([100, 200, 30, 40], [32, 5, 67, 8]), 1)
        self.assertEqual(self.averager.comp_averages([40, 7, 64, 1], [32, 5, 67, 8]), 0)
