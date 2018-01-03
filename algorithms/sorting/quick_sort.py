import random


# Quicksort with O(1) temporary storage space.
def quicksort(items):
    def _quicksort(items, p, r):
        if p < r:
            q = partition(items, p, r)
            _quicksort(items, p, q - 1)
            _quicksort(items, q + 1, r)
    _quicksort(items, 0, len(items) - 1)


def partition(items, p, r):
    pivot = items[r]
    i = p - 1
    for j in range(p, r):
        if items[j] <= pivot:
            i += 1
            items[i], items[j] = items[j], items[i]
    # Move pivot into correct position.
    items[i + 1], items[r] = items[r], items[i + 1]
    return i + 1


# Modified quicksort to use randomized pivot.
def randomized_quicksort(items):
    def _randomized_quicksort(items, p, r):
        if p < r:
            q = randomized_partition(items, p, r)
            _randomized_quicksort(items, p, q - 1)
            _randomized_quicksort(items, q + 1, r)
    _randomized_quicksort(items, 0, len(items) - 1)


def randomized_partition(items, p, r):
    i = random.randint(p, r)
    items[r], items[i] = items[i], items[r]
    return partition(items, p, r)
