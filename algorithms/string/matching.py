def kmp(s, p):
    """Returns the index of the first occurrence of the pattern p as a
    substring in the string s or -1 if p does not occur in s.

    Uses the Knuth-Morris-Pratt algorithm (worst case O(n)).

    Args:
        s (str): The string to check for existence of pattern inside.
        p (str): The pattern to look for inside the string.
    """
    def compute_prefix_function(p):
        """Computes the prefix function pi for pattern p.

        Args:
            p (str): The pattern to generate the prefix function for.

        Returns:
            list: A list pi with length m + 1 where m = len(p).

            The list satisfies the property pi[q] = pi(q) for q = 1, ..., m.
        """
        m = len(p)
        pi = [None] * (m + 1)
        pi[1] = 0
        k = 0
        for q in range(1, m):
            while k > 0 and p[k] != p[q]:
                k = pi[k]
            if p[k] == p[q]:
                k += 1
            pi[q + 1] = k
        return pi

    n, m = len(s), len(p)
    if not m:
        return 0
    if n < m:
        return -1
    pi = compute_prefix_function(p)
    q = 0
    for i in range(n):
        while q > 0 and p[q] != s[i]:
            q = pi[q]
        if p[q] == s[i]:
            q += 1
        if q == m:
            return i - m + 1
    return -1


def rabin_karp(s, p):
    """Returns the index of the first occurrence of the pattern p as a
    substring in the string s or -1 if p does not occur in s.

    Uses the Rabin-Karp algorithm (worst case O(nm)).

    Args:
        s: string to check for existence of pattern inside
        p: pattern to look for inside the string
    """
    n, m = len(s), len(p)
    if not m:
        return 0
    if n < m:
        return -1
    q = 101
    h = pow(256, m - 1, q)
    x = 0
    y = 0
    for i in range(m):
        x = (256 * x + ord(p[i])) % q
        y = (256 * y + ord(s[i])) % q
    for i in range(n - m + 1):
        if x == y and all(s[i + j] == p[j] for j in range(m)):
            return i
        if i < n - m:
            y = (256 * (y - h * ord(s[i])) + ord(s[i + m])) % q
    return -1
