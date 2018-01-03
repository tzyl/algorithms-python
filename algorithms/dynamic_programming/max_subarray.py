# Kadane's algorithm
def max_subarray(array):
    max_ending_here = max_so_far = 0
    for x in array:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
