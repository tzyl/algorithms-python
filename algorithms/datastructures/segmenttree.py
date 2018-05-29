class SegmentTree:

    def __init__(self, A, f, identity):
        """Builds a segment tree from an initial array and a combining
        function and an identity element.

        Args:
            A: list of initial array elements
            f: binary function which combines two segment results into a
               single result
            identity: identity element for the given binary function
        """
        self.tree = [None] * (2 * len(A) - 1)
        self.f = f
        self.identity = identity
        self.n = len(A)
        # Initialize the segment tree.
        self.build_segment_tree(A, 0, 0, len(A) - 1)

    def parent(self, i):
        if i == 0:
            return 0
        return (i - 1) // 2

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def mid(self, start, end):
        return (start + end) // 2

    def query(self, start, end):
        """Returns the value for the segment [start, end].

        Args:
            start: start index of the query segment
            end: end index of the query segment
        """
        return self._query(0, 0, self.n - 1, start, end)

    def _query(self, i, c_start, c_end, q_start, q_end):
        """Returns the contribution to the query of the current node.

        Args:
            i: current index in the segment tree
            c_start: start index of the current segment
            c_end: end index of the current segment
            q_start: start index of the query segment
            q_end: end index of the query segment
        """
        if c_start >= q_start and c_end <= q_end:
            # Whole segment is contained.
            return self.tree[i]
        elif c_start > q_end or c_end < q_start:
            # None of segment overlaps.
            return self.identity
        else:
            # Partial segment overlap.
            c_mid = self.mid(c_start, c_end)
            return self.f(
                self._query(self.left(i), c_start, c_mid, q_start, q_end),
                self._query(self.right(i), c_mid + 1, c_end, q_start, q_end)
            )

    def update(self, idx, x):
        """Updates the value at the array index i to be x.

        Args:
            idx: index in the original array to update
            x: the new value
        """
        self._update(0, 0, self.n - 1, idx, x)

    def _update(self, i, c_start, c_end, idx, x):
        """Updates the current node in the segment tree.

        Args:
            i: current index in the segment tree
            c_start: start index of the current segment
            c_end: end index of the current segment
            x: the new value
            idx: index in the original array to update
        """
        if c_start > idx or c_end < idx:
            # Index to update is outside of current segment
            return self.tree[i]
        elif c_start == c_end:
            # At leaf node of index to update
            self.tree[i] = x
            return self.tree[i]
        else:
            # Leaf node of index to update is contained in current segment.
            c_mid = self.mid(c_start, c_end)
            self.tree[i] = self.f(
                self._update(self.left(i), c_start, c_mid, idx, x),
                self._update(self.right(i), c_mid + 1, c_end, idx, x)
            )
            return self.tree[i]

    def build_segment_tree(self, A, i, start, end):
        """Recursively builds the segment tree from root index i.

        Args:
            A: list of initial array elements
            i: current index in the segment tree
            start: start index of the current segment
            end: end index of the current segment
        """
        if start == end:
            self.tree[i] = A[start]
            return self.tree[i]

        mid = self.mid(start, end)
        self.tree[i] = self.f(
            self.build_segment_tree(A, self.left(i), start, mid),
            self.build_segment_tree(A, self.right(i), mid + 1, end)
        )
        return self.tree[i]
