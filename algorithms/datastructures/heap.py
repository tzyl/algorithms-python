class MinHeap:
    def __init__(self, heap_array):
        self.heap_array = heap_array
        self.heap_size = len(heap_array)
        self.build_min_heap()

    def parent(self, i):
        if i == 0:
            return 0
        return (i - 1) // 2

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def check_min_heap_property(self):
        A = self.heap_array
        for i in reversed(range(1, self.heap_size)):
            if A[i] < A[self.parent(i)]:
                print(i, self.parent(i))
                print(A[i], A[self.parent(i)])
                return False
        return True

    def min_heapify(self, i):
        A = self.heap_array
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < self.heap_size and A[l] < A[smallest]:
            smallest = l
        if r < self.heap_size and A[r] < A[smallest]:
            smallest = r
        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            self.min_heapify(smallest)

    def build_min_heap(self):
        for i in reversed(range(self.heap_size // 2)):
            self.min_heapify(i)


class MaxHeap:
    def __init__(self, heap_array):
        self.heap_array = heap_array
        self.heap_size = len(heap_array)
        self.build_max_heap()

    @staticmethod
    def parent(i):
        if i == 0:
            return 0
        return (i - 1) // 2

    @staticmethod
    def left(i):
        return 2 * (i + 1) - 1

    @staticmethod
    def right(i):
        return 2 * (i + 1)

    def check_max_heap_property(self):
        A = self.heap_array
        for i in reversed(range(1, self.heap_size)):
            if A[i] > A[self.parent(i)]:
                print(i, self.parent(i))
                print(A[i], A[self.parent(i)])
                return False
        return True

    def max_heapify(self, i):
        A = self.heap_array
        l = MaxHeap.left(i)
        r = MaxHeap.right(i)
        largest = i
        if l < self.heap_size and A[l] > A[largest]:
            largest = l
        if r < self.heap_size and A[r] > A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in reversed(range(self.heap_size // 2)):
            self.max_heapify(i)

# 1-index
# class MaxHeap2:
#     def __init__(self, heap_array):
#         self.heap_array = None
#         self.heap_size = None
#         # Initialize the max heap.
#         self.build_max_heap(heap_array)

#     @staticmethod
#     def parent(i):
#         return i // 2

#     @staticmethod
#     def left(i):
#         return 2 * i

#     @staticmethod
#     def right(i):
#         return 2 * i + 1

#     def max_heapify(self, i):
#         A = self.heap_array
#         l = MaxHeap2.left(i)
#         r = MaxHeap2.right(i)
#         largest = i
#         if l <= self.heap_size and A[l] > A[i]:
#             largest = l
#         if r <= self.heap_size and A[r] > A[largest]:
#             largest = r
#         if largest != i:
#             A[i], A[largest] = A[largest], A[i]
#             self.max_heapify(largest)

#     def build_max_heap(self, heap_array):
#         # Modifies the heap_array in place to represent a max heap.
#         self.heap_size = len(heap_array)
#         # Add None in first place so we can 1-index.
#         self.heap_array = [None] + heap_array
#         for i in range(self.heap_size // 2, 0, -1):
#             self.max_heapify(i)


def heapsort(unsorted):
    max_heap = MaxHeap(unsorted)
    A = max_heap.heap_array
    for i in reversed(range(1, len(unsorted))):
        A[0], A[i] = A[i], A[0]
        max_heap.heap_size -= 1
        max_heap.max_heapify(0)

# if __name__ == "__main__":
#     import random
#     unsorted = [random.randint(0, 1000) for i in range(100)]
#     heapsort(unsorted)
#     print(unsorted == sorted(unsorted))
#     # print(heapsort2(unsorted) == sorted(unsorted))
#     max_heap = MaxHeap(unsorted)
#     print(max_heap.check_max_heap_property())
#     print(max_heap.heap_array)
#     min_heap = MinHeap(unsorted)
#     print(min_heap.check_min_heap_property())
#     print(min_heap.heap_array)
