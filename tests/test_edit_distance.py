import unittest
from algorithms.dynamic_programming.edit_distance import *


class TestEditDistance(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(edit_distance("", ""), 0)

    def test_one_string_empty(self):
        self.assertEqual(edit_distance("abc", ""), 3)
        self.assertEqual(edit_distance("", "abc"), 3)

    def test_insertion(self):
        self.assertEqual(edit_distance("ac", "abc"), 1)

    def test_removal(self):
        self.assertEqual(edit_distance("abc", "ac"), 1)

    def test_substitution(self):
        self.assertEqual(edit_distance("abc", "azc"), 1)
