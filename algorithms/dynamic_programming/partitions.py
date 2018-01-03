def memoize(fn):
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = fn(*args, **kwargs)
        return cache[key]
    cache = {}
    return wrapper


@memoize
def partitions(n):
    """Returns a list of partitions of n where each partition is a unique list
    of descending integers which together sum to n.

    Args:
        n: integer to create partitions from
    """
    result = [[n]]
    # Iterate over largest element of partition.
    for i in range(1, n):
        m = n - i
        for p in partitions(m):
            if p[0] <= i:
                result.append([i] + p)
    return result


# if __name__ == '__main__':
#     print(len(partitions(19)))
#     print(partitions(5))
