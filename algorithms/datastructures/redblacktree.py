from enum import Enum


class RedBlackTree:
    def __init__(self):
        self.nil = RedBlackNode(None)
        self.nil.color = Color.black
        self.root = self.nil

    def insert(self, x):
        y = self.nil
        z = self.root
        while z is not self.nil:
            y = z
            if x.key < z.key:
                z = z.left
            else:
                z = z.right
        x.parent = y
        if y is self.nil:
            self.root = x
        elif x.key < y.key:
            y.left = x
        else:
            y.right = x
        x.left = self.nil
        x.right = self.nil
        x.color = Color.red
        self.red_black_fixup(x)

    def red_black_fixup(self, x):
        while x.parent.color is Color.red:
            if x.parent is x.parent.parent.left:
                y = x.parent.parent.right
                if y.color is Color.red:
                    # Case 1
                    x.parent.color = Color.black
                    y.color = Color.black
                    x.parent.parent.color = Color.red
                    x = x.parent.parent
                else:
                    if x is x.parent.right:
                        # Case 2
                        x = x.parent
                        self.left_rotate(x)
                    # Case 3
                    x.parent.color = Color.black
                    x.parent.parent.color = Color.red
                    self.right_rotate(x.parent.parent)
            else:
                y = x.parent.parent.left
                if y.color is Color.red:
                    # Case 1
                    x.parent.color = Color.black
                    y.color = Color.black
                    x.parent.parent.color = Color.red
                    x = x.parent.parent
                else:
                    if x is x.parent.left:
                        # Case 2
                        x = x.parent
                        self.right_rotate(x)
                    # Case 3
                    x.parent.color = Color.black
                    x.parent.parent.color = Color.red
                    self.left_rotate(x.parent.parent)
        self.root.color = Color.black

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y


class Color(Enum):
    red = 0
    black = 1


class RedBlackNode:
    def __init__(self, key):
        self.key = key
        self.color = None
        self.parent = None
        self.left = None
        self.right = None

# if __name__ == '__main__':
#     import random
#     keys = list(range(20))
#     random.shuffle(keys)
#     print(keys)
#     rb_tree = RedBlackTree()
#     for key in keys:
#         rb_tree.insert(RedBlackNode(key))
