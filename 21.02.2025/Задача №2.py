def is_cyclic_util(v, visited, parent, adj):
    visited[v] = True

    for i in adj[v]:
        if not visited[i]:
            if is_cyclic_util(i, visited, v, adj):
                return True
        elif parent != i:
            return True

    return False

def is_cyclic(V, adj):
    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            if is_cyclic_util(i, visited, -1, adj):
                return True

    return False


V, E = map(int, input().split())
adj_list = input().strip('{}').split('}, {')
adj_list = [list(map(int, neighbors.split(', '))) for neighbors in adj_list]


adj = [[] for _ in range(V)]
for idx, neighbors in enumerate(adj_list):
    adj[idx].extend(neighbors)


if is_cyclic(V, adj):
    print('YES')
else:
    print('NO')