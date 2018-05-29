# O(n^2) DP solution.
def longest_palindrome_substring(s):
    longest = ""
    # P[i][j] is True if the substring s[i:j+1] is a palindrome.
    P = [[False] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        P[i][i] = True
    for l in range(2, len(s) + 1):
        for i in range(len(s) + 1 - l):
            j = i + l - 1
            if s[i] == s[j] and (j == i + 1 or P[i + 1][j - 1]):
                P[i][j] = True
                longest = max(longest, s[i:j+1], key=len)
    return longest
