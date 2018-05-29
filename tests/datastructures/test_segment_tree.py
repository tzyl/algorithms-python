import unittest
from algorithms.datastructures.segmenttree import SegmentTree


class TestSegmentTree(unittest.TestCase):

    def test_build(self):
        A = [1, 2, 3]
        segment_tree = SegmentTree(A, lambda x, y: x + y, 0)
        self.assertEqual(segment_tree.tree, [6, 3, 3, 1, 2])

    def test_update(self):
        A = [1, 2, 3]
        segment_tree = SegmentTree(A, lambda x, y: x + y, 0)
        self.assertEqual(segment_tree.tree, [6, 3, 3, 1, 2])
        segment_tree.update(0, 4)
        self.assertEqual(segment_tree.tree, [9, 6, 3, 4, 2])

    def test_range_max_query(self):
        A = [1, 2, 3, 0, -1]
        segment_tree = SegmentTree(A, max, -float("inf"))
        self.assertEqual(segment_tree.query(0, len(A) - 1), 3)
        self.assertEqual(segment_tree.query(0, 1), 2)
        self.assertEqual(segment_tree.query(4, 4), -1)
