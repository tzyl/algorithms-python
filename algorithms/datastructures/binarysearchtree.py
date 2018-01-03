class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        y = None
        z = self.root
        while z is not None:
            y = z
            if x.key < z.key:
                z = z.left
            else:
                z = z.right
        x.parent = y
        if y is None:
            self.root = x
        elif x.key < y.key:
            y.left = x
        else:
            y.right = x

    def insert_recursive(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, root, x):
        if root is None:
            return x
        elif x.key < root.key:
            root.left = self._insert(root.left, x)
        else:
            root.right = self._insert(root.right, x)
        return root

    def search(self, k):
        x = self.root
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def search_recursive(self, k):
        return self._search(self.root, k)

    def _search(self, root, k):
        if root is None or k == root.key:
            return root
        elif k < root.key:
            return self._search(root.left, k)
        elif k > root.key:
            return self._search(root.right, k)

    def successor(self, x):
        if x.right is not None:
            return self.minimum(x.right)
        y = x.parent
        while y is not None and x is not y.left:
            x = y
            y = y.parent
        return y

    def predecessor(self, x):
        if x.left is not None:
            return self.maximum(x.left)
        y = x.parent
        while y is not None and x is not y.right:
            x = y
            y = y.parent
        return y

    def minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def maximum(self, x):
        while x.right is not None:
            x = x.right
        return x

    def transplant(self, u, v):
        """Transplants the subtree rooted at node v to replace the subtree
        rooted at node u."""
        if u.parent is None:
            self.root = v
        elif u.parent.left is u:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def delete(self, x):
        if x.left is None:
            self.transplant(x, x.right)
        elif x.right is None:
            self.transplant(x, x.left)
        else:
            y = self.minimum(x.right)
            if y.parent is not x:
                self.transplant(y, y.right)
                y.right = x.right
                y.right.parent = y
            self.transplant(x, y)
            y.left = x.left
            y.left.parent = y


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


# if __name__ == "__main__":
#     import random
#     bst = BinarySearchTree2()
#     nodes = [(random.randint(0, 100),)*2 for x in range(10)]
#     for node in nodes:
#         bst.put(node[0], node[1])
#     bst.draw()
