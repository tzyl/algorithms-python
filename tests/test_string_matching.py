import unittest
from algorithms.string.matching import rabin_karp, kmp


class TestStringMatching(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(rabin_karp("", ""), 0)
        self.assertEqual(kmp("", ""), 0)

    def test_empty_string_contained(self):
        self.assertEqual(rabin_karp("abc", ""), 0)
        self.assertEqual(kmp("abc", ""), 0)

    def test_empty_string_contains(self):
        self.assertEqual(rabin_karp("", "abc"), -1)
        self.assertEqual(kmp("", "abc"), -1)

    def test_basic(self):
        self.assertEqual(rabin_karp("abcdefg", "cde"), 2)
        self.assertEqual(kmp("abcdefg", "cde"), 2)

    def test_no_match(self):
        self.assertEqual(rabin_karp("abc", "def"), -1)
        self.assertEqual(kmp("abc", "def"), -1)

    def test_first_match(self):
        self.assertEqual(rabin_karp("xxxABCxxxABCxxx", "ABC"), 3)
        self.assertEqual(kmp("xxxABCxxxABCxxx", "ABC"), 3)
