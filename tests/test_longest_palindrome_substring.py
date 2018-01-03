import unittest
from algorithms.dynamic_programming.longest_palindrome_substring import *


class TestLongestPalindromeSubstring(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(len(longest_palindrome_substring("")), 0)

    def test_example(self):
        self.assertEqual(len(longest_palindrome_substring("zzzabcdcbaxxx")), 7)

    def test_long_string(self):
        self.assertEqual(len(longest_palindrome_substring("a" * 1000)), 1000)
