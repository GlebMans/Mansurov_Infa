def dfs(v, visited, graph):
    stack = [v]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)

def count_connected_components(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, graph)
            count += 1

    return count

n = int(input())
m = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

result = count_connected_components(n, edges)

print(result)