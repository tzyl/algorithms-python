import random


def shuffle(A):
    """Fisher-Yates shuffle."""
    for i in range(len(A)):
        j = random.randint(i, len(A) - 1)
        A[i], A[j] = A[j], A[i]


def random_sample(m, n):
    """Returns a random sample of m integers from [1,...,n] as a list."""
    if m == 0:
        return []
    else:
        S = random_sample(m - 1, n - 1)
        i = random.randint(1, n)
        if i in S:
            S.append(n)
        else:
            S.append(i)
        return S


# if __name__ == '__main__':
#     A = list(range(10))
#     for i in range(10):
#         shuffle(A)
#         print(A)
#     for i in range(10):
#         print(random_sample(10, 100))
