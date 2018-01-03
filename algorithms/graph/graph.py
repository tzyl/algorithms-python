from enum import Enum
from algorithms.datastructures.queue import Queue
from algorithms.datastructures.priorityqueue import MinPriorityQueue


class Color(Enum):
    white = 0
    gray = 1
    black = 2


class Graph:
    def __init__(self, n, E):
        self.count = 0
        self.V = []
        self.Adj = [[] for _ in range(n)]
        for i in range(n):
            self.V.append(Node(i))
        for e in E:
            self.Adj[e[0]].append(self.V[e[1]])
            self.Adj[e[1]].append(self.V[e[0]])


class DirectedGraph:
    def __init__(self, n, E):
        self.count = 0
        self.V = []
        self.Adj = [[] for _ in range(n)]
        for i in range(n):
            self.V.append(Node(i))
        for e in E:
            self.Adj[e[0]].append(self.V[e[1]])


class Node:
    def __init__(self, key):
        self.key = key
        self.color = None
        self.d = None
        self.p = None


def bfs(G, s):
    for v in G.V:
        v.color = Color.white
        v.d = float("inf")
        v.p = None
    s.color = Color.gray
    s.d = 0
    s.p = None
    Q = Queue()
    Q.enqueue(s)
    while not Q.queue_empty():
        u = Q.dequeue()
        for v in G.Adj[u.key]:
            if v.color is Color.white:
                v.color = Color.gray
                v.d = u.d + 1
                v.p = u
                Q.enqueue(v)
        u.color = Color.black


def dfs(G):
    for u in G.V:
        u.color = Color.white
        u.p = None
    t = 0
    for u in G.V:
        if u.color is Color.white:
            t = dfs_visit(G, u, t)


def dfs_visit(G, u, t):
    t += 1
    u.d = t
    u.color = Color.gray
    for v in G.Adj[u.key]:
        if v.color is Color.white:
            v.p = u
            t = dfs_visit(G, v, t)
    u.color = Color.black
    t += 1
    u.f = t
    return t


# s is source, w is weight function of edges.
def dijkstra(G, w, s):
    for v in G.V:
        v.d = float("inf")
        v.p = None
    s.d = 0
    S = set()
    Q = MinPriorityQueue([G.V])
    while Q.heap_size:
        u = Q.extract_min()
        S.add(u)
        for v in G.Adj[u.key]:
            if v.d > u.d + w(u, v):
                v.d = u.d + w(u, v)
                v.p = u


def topological_sort(G):
    def dfs_visit(v):
        visited.add(v)
        for w in G.Adj[v.key]:
            if w not in visited:
                dfs_visit(w)
        finished.append(v)

    finished = []
    visited = set()
    for v in G.V:
        if v not in visited:
            dfs_visit(v)
    return finished[::-1]


# if __name__ == '__main__':
#     G = Graph(4, [(0, 1), (1, 2), (2, 3)])
#     # bfs(G, G.V[0])
#     # dfs(G)
#     # for v in G.V:
#         # print(v.d, v.f)
#     G = DirectedGraph(4, [(1, 0), (2, 1), (3, 2)])
#     print([v.key for v in topological_sort(G)])
#     G = DirectedGraph(4, [(0, 3), (3, 2), (2, 1)])
#     print([v.key for v in topological_sort(G)])
