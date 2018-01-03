# Recursive tree traversals.
def preorder_traversal(root):
    print(root)
    if root.left is not None:
        preorder_traversal(root.left)
    if root.right is not None:
        preorder_traversal(root.right)


def inorder_traversal(root):
    if root.left is not None:
        preorder_traversal(root.left)
    print(root)
    if root.right is not None:
        preorder_traversal(root.right)


def postorder_traversal(root):
    if root.left is not None:
        preorder_traversal(root.left)
    if root.right is not None:
        preorder_traversal(root.right)
    print(root)


# Iterative tree traversals.
def preorder_iterative(root):
    if root is None:
        return
    stack = [root]
    while stack:
        current = stack.pop()
        print(current)
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)


def inorder_iterative(root):
    if root is None:
        return
    stack = []
    current = root
    while current is not None:
        stack.append(current)
        current = current.left
    while stack:
        current = stack.pop()
        print(current)
        current = current.right
        while current is not None:
            stack.append(current)
            current = current.left


def postorder_iterative(root):
    if root is None:
        return
    stack1 = [root]
    stack2 = []
    # Preorder traversal but right child before left child then reverse this
    # using stack2 to get postorder traversal.
    while stack1:
        current = stack1.pop()
        stack2.append(current)
        if current.left is not None:
            stack1.append(current.left)
        if current.right is not None:
            stack1.append(current.right)
    while stack2:
        print(stack2.pop())
