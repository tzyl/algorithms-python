from .linkedlist import LinkedList, Node


class Stack(LinkedList):
    """Linked list implementation of Stack."""
    def __init__(self):
        super(Stack, self).__init__()

    def stack_empty(self):
        return self.empty()

    def push(self, x):
        self.insert(Node(x))

    def pop(self):
        if self.stack_empty():
            raise Exception("Stack underflow")
        value = self.head.key
        self.delete(self.head)
        return value

    def peek(self):
        if self.stack_empty():
            raise Exception("Stack underflow")
        return self.head.key


class StackArray:
    """Array implementation of Stack."""
    def __init__(self, n):
        self.n = n
        self.data = [None] * n
        self.top = -1

    def stack_empty(self):
        return self.top == -1

    def stack_full(self):
        return self.top == self.n - 1

    def push(self, x):
        if self.stack_full():
            raise Exception("Stack overflow")
        self.top += 1
        self.data[self.top] = x

    def pop(self):
        if self.stack_empty():
            raise Exception("Stack underflow")
        value = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.stack_empty():
            raise Exception("Stack underflow")
        return self.data[self.top]

# if __name__ == "__main__":
#     stack = StackArray(3)
#     for i in range(3):
#         stack.push(i)
#         print(stack.data)
#         print("Stack full: %s" % stack.stack_full())
#     for i in range(3):
#         print(stack.pop())
#         print(stack.data)
#         print("Stack empty: %s" % stack.stack_empty())
