from algorithms.dynamicprogramming.longest_common_subsequence import \
    longest_common_subsequence


def longest_palindrome_subsequence(s):
    """USING DP O(n^2)"""
    A = [[1] * len(s) for _ in range(len(s))]
    B = [[None] * len(s) for _ in range(len(s))]
    for length in range(2, len(s) + 1):
        for i in range(len(s) - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if j == i + 1:
                    A[i][j] = 2
                else:
                    A[i][j] = A[i + 1][j - 1] + 2
                    B[i][j] = "down-left"
            elif s[i] != s[j]:
                if A[i + 1][j] > A[i][j - 1]:
                    A[i][j] = A[i + 1][j]
                    B[i][j] = "down"
                else:
                    A[i][j] = A[i][j - 1]
                    B[i][j] = "left"
    lps = get_lps(s, A, B)
    return lps


def get_lps(s, A, B):
    i, j = 0, len(s) - 1
    palindrome_chars = []
    while B[i][j] is not None:
        if B[i][j] == "down-left":
            palindrome_chars.append(s[i])
            i, j = i + 1, j - 1
        elif B[i][j] == "down":
            i += 1
        elif B[i][j] == "left":
            j -= 1
    return ("".join(palindrome_chars) +
            s[i:j+1] +
            "".join(palindrome_chars[::-1]))


def longest_palindrome_subsequence2(s):
    """USING LCS O(n^2)"""
    s1 = s
    s2 = s[::-1]
    lps = longest_common_subsequence(s1, s2)
    return lps
