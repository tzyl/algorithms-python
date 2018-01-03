from .heap import MaxHeap, MinHeap


class MaxPriorityQueue(MaxHeap):
    def maximum(self):
        return self.heap_array[0]

    def extract_max(self):
        if self.heap_size == 0:
            return "Error! Heap underflow."
        A = self.heap_array
        max_ = self.maximum()
        A[0] = A[self.heap_size - 1]
        self.heap_size -= 1
        A.pop()
        self.max_heapify(0)
        return max_

    def increase_key(self, i, key):
        A = self.heap_array
        if key < A[i]:
            return "Error! New key is smaller than current key"
        A[i] = key
        while i > 0 and A[i] > A[self.parent(i)]:
            A[i], A[self.parent(i)] = A[self.parent(i)], A[i]
            i = self.parent(i)

    def insert(self, key):
        self.heap_size += 1
        self.heap_array.append(-float("inf"))
        # self.heap_array[self.heap_size] = -float("inf")
        self.increase_key(self.heap_size - 1, key)


class MinPriorityQueue(MinHeap):
    def minimum(self):
        return self.heap_array[0]

    def extract_min(self):
        if self.heap_size == 0:
            return "Error! Heap underflow."
        A = self.heap_array
        min_ = A[0]
        A[0] = A[self.heap_size - 1]
        self.heap_size -= 1
        A.pop()
        self.min_heapify(0)
        return min_

    def decrease_key(self, i, key):
        A = self.heap_array
        if key > A[i]:
            return "Error! New key is larger than current key."
        A[i] = key
        while i > 0 and A[i] < A[self.parent(i)]:
            A[i], A[self.parent(i)] = A[self.parent(i)], A[i]
            i = self.parent(i)

    def insert(self, key):
        self.heap_size += 1
        self.heap_array.append(float("inf"))
        self.decrease_key(self.heap_size - 1, key)

# if __name__ == '__main__':
#     min_pq = MinPriorityQueue([])
#     max_pq = MaxPriorityQueue([])
#     for i in range(100):
#         min_pq.insert(i)
#         max_pq.insert(i)
#     print(min_pq.heap_array)
#     print(max_pq.heap_array)
