def longest_common_subsequence(s1, s2):
    A = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    B = [[None] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                A[i + 1][j + 1] = A[i][j] + 1
                B[i + 1][j + 1] = "up-left"
            elif A[i][j + 1] > A[i + 1][j]:
                A[i + 1][j + 1] = A[i][j + 1]
                B[i + 1][j + 1] = "up"
            else:
                A[i + 1][j + 1] = A[i + 1][j]
                B[i + 1][j + 1] = "left"
    lcs = get_lcs(s1, s2, A, B)
    return lcs


def get_lcs(s1, s2, A, B):
    i, j = len(s1), len(s2)
    lcs_chars = []
    while i > 0 and j > 0:
        if B[i][j] == "up-left":
            lcs_chars.append(s1[i - 1])
            i, j = i - 1, j - 1
        elif B[i][j] == "up":
            i -= 1
        elif B[i][j] == "left":
            j -= 1
    return "".join(lcs_chars[::-1])
