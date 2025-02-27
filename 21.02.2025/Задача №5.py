from collections import deque

def bfs(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    distances = [-1] * n
    distances[0] = 0

    queue = deque([0])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

distances = bfs(n, edges)

for distance in distances:
    print(distance)