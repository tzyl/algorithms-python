from .linkedlist import LinkedListWithTail, Node


class Queue(LinkedListWithTail):
    """Linked list implementation of Queue."""
    def __init__(self):
        super(Queue, self).__init__()

    def queue_empty(self):
        return self.empty()

    def enqueue(self, x):
        self.insert_tail(Node(x))

    def dequeue(self):
        if self.queue_empty():
            return None
        value = self.head.key
        self.delete(self.head)
        return value

    def peek(self):
        if self.queue_empty():
            return None
        return self.head.key


class QueueArray:
    """Array implementation of Queue."""
    def __init__(self, n):
        self.data = [None] * (n + 1)
        self.head = self.tail = 0

    def queue_empty(self):
        return self.head == self.tail

    def queue_full(self):
        return self.head == (self.tail + 1) % len(self.data)

    def enqueue(self, x):
        if self.queue_full():
            raise Exception("Queue overflow")
        self.data[self.tail] = x
        self.tail = (self.tail + 1) % len(self.data)

    def dequeue(self):
        if self.queue_empty():
            raise Exception("Queue underflow")
        x = self.data[self.head]
        # self.data[self.head] = None
        self.head = (self.head + 1) % len(self.data)
        return x

    def peek(self):
        if self.queue_empty():
            raise Exception("Queue underflow")
        return self.data[self.head]

# if __name__ == "__main__":
#     queue = QueueArray(5)
#     for i in range(5):
#         queue.enqueue(i)
#         print(queue.data)
#         print("Queue full: %s" % queue.queue_full())
#     for i in range(5):
#         print(queue.dequeue())
#         print(queue.data)
#         print("Queue empty: %s" % queue.queue_empty())
