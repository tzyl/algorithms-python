# O(m*n^2) with adjacency matrix implementation. (O(m*E) with adjacency list)
def maximum_bipartite_matching(A, m, n):
    """Returns the maximum size of a matching in the bipartite graph
    described by A.

    Uses simplified Ford-Fulkerson method with DFS to find matches as
    capacities can only be either 0 or 1.

    Parameters:
    A - m x n matrix representing edges between the two vertex partitions.
    m - number of vertices in the left vertex partition.
    n - number of vertices in the right vertex partition.
    """
    def dfs(u, seen):
        for v in range(n):
            if A[u][v]:
                if seen[v]:
                    continue
                seen[v] = True
                if match_R[v] is None or dfs(match_R[v], seen):
                    match_L[u] = v
                    match_R[v] = u
                    return True
                return False

    match_L = [None] * m
    match_R = [None] * n
    count = 0
    for i in range(m):
        # Reset vertices seen for DFS for this vertex.
        seen = [False] * n
        if dfs(i, seen):
            count += 1
    return count
