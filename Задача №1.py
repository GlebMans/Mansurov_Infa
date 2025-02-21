from collections import defaultdict
def find_social_clusters(n, relationships):

    def dfs(node, graph, visited, stack):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, graph, visited, stack)
        stack.append(node)

    def reverse_dfs(node, reverse_graph, visited, component):
        visited[node] = True
        component.append(node)
        for neighbor in reverse_graph[node]:
            if not visited[neighbor]:
                reverse_dfs(neighbor, reverse_graph, visited, component)

    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    for u, v in relationships:
        graph[u].append(v)
        reverse_graph[v].append(u)

    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            dfs(i, graph, visited, stack)

    visited = [False] * n
    clusters = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            reverse_dfs(node, reverse_graph, visited, component)
            clusters.append(sorted(component))

    clusters.sort(key=lambda x: (-len(x), x))
    return clusters

n = 5
relationships = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4), (4, 3)]
print(find_social_clusters(n, relationships))