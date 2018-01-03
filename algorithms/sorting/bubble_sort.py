def bubble_sort(items):
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if not swapped:
            return
