import unittest
from algorithms.graph.graph import *


class TestGraphAlgorithms(unittest.TestCase):

    def test_topological_sort(self):
        self.assertEqual(
            [3, 2, 1, 0],
            [v.key for v in topological_sort(DirectedGraph(4, [(1, 0), (2, 1), (3, 2)]))]
        )
        self.assertEqual(
            [0, 3, 2, 1],
            [v.key for v in topological_sort(DirectedGraph(4, [(0, 3), (3, 2), (2, 1)]))]
        )
