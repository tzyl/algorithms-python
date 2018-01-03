def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    # dp[i][j] is the edit distance between s1[:i] and s2[:j].
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # Remove s1[i]
                                   dp[i][j - 1],      # Insert s1[i]
                                   dp[i - 1][j - 1])  # Substitute s1[i - 1] for s2[j - 1]
    return dp[m][n]
