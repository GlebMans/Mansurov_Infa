from collections import deque
from collections import defaultdict

def sorting(n, m, edges):
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    order = []
    
    while queue:
        if len(queue) > 1:
            return "NO"
        current = queue.popleft()
        order.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return "-1" if len(order) != n else "YES"

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for i in range(m)]
print(sorting(n, m, edges))