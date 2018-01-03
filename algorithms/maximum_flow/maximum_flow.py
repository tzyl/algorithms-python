from collections import deque


class AdjacencyList:
    def __init__(self, n):
        self.adjacency_list = [[] for vertex in range(n)]

    def __getitem__(self, arg):
        return self.adjacency_list[arg]

    def __len__(self):
        return len(self.adjacency_list)

    def add_directed_edge(self, u, v, c):
        """Adds a directed Edge from u to v with capacity c and also a directed
        reverse Edge from v to u with capacity 0.
        """
        edge = Edge(u, v, c)
        reverse_edge = Edge(u, v, 0)
        edge.reverse = reverse_edge
        reverse_edge.reverse = edge
        self.adjacency_list[u].append(edge)
        self.adjacency_list[v].append(reverse_edge)

    def add_undirected_edge(self, u, v, c):
        """Adds two directed edges with capacity c, one from u to v and another
        from v to u.
        """
        edge = Edge(u, v, c)
        reverse_edge = Edge(u, v, c)
        edge.reverse = reverse_edge
        reverse_edge.reverse = edge
        self.adjacency_list[u].append(edge)
        self.adjacency_list[v].append(reverse_edge)


class Edge:
    def __init__(self, u, v, c):
        self.start = u
        self.end = v
        self.capacity = c
        self.flow = 0
        self.reverse = None


# O(V*E^2) with adjacency list implementation. (O(V^3*E) if adjacency matrix)
def ford_fulkerson(A, s, t):
    """Returns the maximum flow possible in a network using the Ford-Fulkerson
    method.

    Args:
        A: AdjacencyList of network where A[v] contains Edge objects
           representing directed edges starting from v.
        s: index of source vertex
        t: index of sink vertex
    """
    max_flow = 0
    residual_capacity = find_augmenting_path(A, s, t)
    while residual_capacity:
        # We found an augmenting path.
        max_flow += residual_capacity
        residual_capacity = find_augmenting_path(A, s, t)
    return max_flow


def find_augmenting_path(A, s, t):
    """Returns the residual capacity of the augmenting path found using BFS
    (Edmonds-Karp algorithm) or returns 0 if no augmenting path exists.

    Updates flows of edges. Residual network implicit from edge capacities and
    flows.

    Args:
        A: AdjacencyList of network where A[v] contains Edge objects
           representing directed edges starting from v.
        s: index of source vertex
        t: index of sink vertex
    """
    queue = deque([s])
    residual_capacity = 0
    # edge_from[v] points to the Edge used to get to v in the BFS.
    edge_from = [None for vertex in range(len(A))]
    while queue:
        u = queue.popleft()
        if u == t:
            # Found an augmenting path. Let's exit early.
            break
        # Check neighbours for possible paths to sink.
        for e in A[u]:
            if edge_from[e.end] is None and e.end != s:
                # This neighbour has not been visited yet.
                if e.capacity > e.flow:
                    # There is residual capacity to augment this edge.
                    edge_from[e.end] = e
                    queue.append(e.end)
    if edge_from[t] is not None:
        # An augmenting path exists.
        residual_capacity = float("inf")
        # Find the path residual capacity.
        e = edge_from[t]
        while e is not None:
            residual_capacity = min(residual_capacity, e.capacity)
            e = edge_from[e.start]
        # Update the flows along the edges we augmented.
        e = edge_from[t]
        while e is not None:
            e.flow += residual_capacity
            e.reverse.flow -= residual_capacity
            e = edge_from[e.start]
    return residual_capacity
