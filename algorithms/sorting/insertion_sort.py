def insertion_sort(items):
    for k in range(1, len(items)):
        j = k
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
