class LinkedList:
    """Doubly linked list"""
    def __init__(self):
        self.head = None

    def __iter__(self):
        x = self.head
        while x is not None:
            yield x
            x = x.next

    def empty(self):
        return self.head is None

    def search(self, k):
        """Searches for the node with key k and returns it or returns None if
        no such node exists."""
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def insert(self, x):
        """Inserts node x into the linked list."""
        x.next = self.head
        if not self.empty():
            self.head.prev = x
        self.head = x
        x.prev = None

    def delete(self, x):
        """Deletes the node x from .the linked list."""
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev

    def traverse(self):
        print("KEY PREV NEXT")
        x = self.head
        while x is not None:
            print("%s\t%s\t%s" % (x.key,
                                  x.prev.key if x.prev is not None else None,
                                  x.next.key if x.next is not None else None))
            x = x.next


class LinkedListWithTail:
    """Doubly linked list with insert to tail."""
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def search(self, k):
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def insert(self, x):
        x.next = self.head
        if not self.empty():
            self.head.prev = x
        else:
            self.tail = x
        self.head = x
        x.prev = None

    def insert_tail(self, x):
        x.prev = self.tail
        if not self.empty():
            self.tail.next = x
        else:
            self.head = x
        self.tail = x
        x.next = None

    def delete(self, x):
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev
        else:
            self.tail = x.prev

    def traverse(self):
        print("KEY PREV NEXT")
        x = self.head
        while x is not None:
            print("%s\t%s\t%s" % (x.key,
                                  x.prev.key if x.prev is not None else None,
                                  x.next.key if x.next is not None else None))
            x = x.next


class LinkedListSentinel:
    """Doubly linked list with sentinel."""
    def __init__(self):
        self.nil = Node(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def empty(self):
        return self.nil.next is self.nil

    def search(self, k):
        """Searches for the node with key k and returns it or returns None if
        no such node exists."""
        x = self.nil.next
        while x is not self.nil and x.key != k:
            print(x.key)
            x = x.next
        return x if x is not self.nil else None

    def insert(self, x):
        """Inserts node x into the linked list."""
        x.next = self.nil.next
        self.nil.next.prev = x
        self.nil.next = x
        x.prev = self.nil

    def delete(self, x):
        """Deletes the node x from .the linked list."""
        x.prev.next = x.next
        x.next.prev = x.prev


class SinglyLinkedList:
    """Singly linked list"""
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None

    def search(self, k):
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def insert(self, x):
        x.next = self.head
        self.head = x
        x.prev = None

    def delete(self, x):
        current = self.head
        if x is current:
            self.head = x.next
        elif current is not None:
            while current.next is not None:
                if x is current.next:
                    current.next = x.next
                    break
                current = current.next


class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

# if __name__ == "__main__":
#     ll = LinkedListWithTail()
#     for i in range(10):
#         ll.insert(Node(i))
#     ll.traverse()
#     for i in range(10):
#         ll.insert_tail(Node(i))
#     ll.traverse()
#     x = ll.head
#     while x is not None:
#         ll.delete(x)
#         x = x.next
