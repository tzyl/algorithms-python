class BinaryIndexedTree:

    def __init__(self, A):
        """Builds a binary indexed tree from an initial array."""
        self.tree = [0] * len(A)
        self.n = len(A)
        # Initialize the binary indexed tree.
        for i, x in enumerate(A):
            self.update(i, x)

    def prefix_sum(self, i):
        """Returns the prefix sum A[0] + ... + A[i]."""
        i += 1
        prefix_sum = 0
        while i > 0:
            prefix_sum += self.tree[i - 1]
            i -= self.least_significant_bit(i)
        return prefix_sum

    def update(self, i, x):
        """Updates the value at the array index i to be x."""
        i += 1
        while i <= self.n:
            self.tree[i - 1] += x
            i += self.least_significant_bit(i)

    def least_significant_bit(self, x):
        return x & -x
