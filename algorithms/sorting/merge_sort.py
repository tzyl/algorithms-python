def merge_sort(items):
    if len(items) <= 1:
        return
    n = len(items) // 2
    left = items[:n]
    right = items[n:]
    merge_sort(left)
    merge_sort(right)
    merge(items, left, right)


def merge(items, left, right):
    i = 0
    j = 0
    for k in range(len(items)):
        if i >= len(left):
            items[k] = right[j]
            j += 1
        elif j >= len(right):
            items[k] = left[i]
            i += 1
        elif left[i] < right[j]:
            items[k] = left[i]
            i += 1
        else:
            items[k] = right[j]
            j += 1
