import unittest
from algorithms.datastructures.binaryindexedtree import BinaryIndexedTree


class TestBinaryIndexedTree(unittest.TestCase):

    def test_build(self):
        A = [1, 2, 3, 4, 5]
        binary_indexed_tree = BinaryIndexedTree(A)
        self.assertEqual(binary_indexed_tree.tree, [1, 3, 3, 10, 5])

    def test_prefix_sum(self):
        A = [1, 2, 3, 4, 5]
        binary_indexed_tree = BinaryIndexedTree(A)
        self.assertEqual(binary_indexed_tree.prefix_sum(0), 1)
        self.assertEqual(binary_indexed_tree.prefix_sum(1), 3)
        self.assertEqual(binary_indexed_tree.prefix_sum(2), 6)
        self.assertEqual(binary_indexed_tree.prefix_sum(3), 10)
        self.assertEqual(binary_indexed_tree.prefix_sum(4), 15)
