import sys
import heapq
import math
from collections import defaultdict, deque

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False

def kruskal(n, edges):
    dsu = DSU(n)
    mst_weight = 0
    mst_edges = []
    mst_graph = defaultdict(list)
    
    edges.sort(key=lambda x: x[2])
    
    for u, v, w, idx in edges:
        if dsu.union(u, v):
            mst_weight += w
            mst_edges.append((u, v, w))
            mst_graph[u].append((v, w))
            mst_graph[v].append((u, w))
    
    return mst_weight, mst_edges, mst_graph

def preprocess_lca(n, mst_graph):
    LOG = math.ceil(math.log2(n)) + 1
    parent = [[-1] * LOG for _ in range(n)]
    max_weight = [[0] * LOG for _ in range(n)]
    depth = [-1] * n

    q = deque([(0, -1, 0)])
    depth[0] = 0

    while q:
        node, par, d = q.popleft()
        parent[node][0] = par
        for v, w in mst_graph[node]:
            if v == par:
                continue
            depth[v] = d + 1
            max_weight[v][0] = w
            q.append((v, node, d + 1))

    for j in range(1, LOG):
        for i in range(n):
            if parent[i][j - 1] != -1:
                parent[i][j] = parent[parent[i][j - 1]][j - 1]
                max_weight[i][j] = max(max_weight[i][j - 1], max_weight[parent[i][j - 1]][j - 1])

    return parent, max_weight, depth

def get_max_weight(u, v, parent, max_weight, depth):
    if depth[u] < depth[v]:
        u, v = v, u
    
    LOG = len(parent[0])
    max_w = 0

    for j in range(LOG - 1, -1, -1):
        if depth[u] - (1 << j) >= depth[v]:
            max_w = max(max_w, max_weight[u][j])
            u = parent[u][j]

    if u == v:
        return max_w

    for j in range(LOG - 1, -1, -1):
        if parent[u][j] != parent[v][j]:
            max_w = max(max_w, max_weight[u][j], max_weight[v][j])
            u = parent[u][j]
            v = parent[v][j]

    return max(max_w, max_weight[u][0], max_weight[v][0])

def find_modified_mst(n, m, edges):
    edges = [(u - 1, v - 1, w, i) for i, (u, v, w) in enumerate(edges)]
    mst_weight, mst_edges, mst_graph = kruskal(n, edges)

    parent, max_weight, depth = preprocess_lca(n, mst_graph)
    mst_set = set((min(u, v), max(u, v)) for u, v, w in mst_edges)

    results = [0] * m
    for u, v, w, idx in edges:
        if (min(u, v), max(u, v)) in mst_set:
            results[idx] = mst_weight
        else:
            max_w = get_max_weight(u, v, parent, max_weight, depth)
            results[idx] = mst_weight - max_w + w

    return results

n, m = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

results = find_modified_mst(n, m, edges)

for res in results:
    print(res)
