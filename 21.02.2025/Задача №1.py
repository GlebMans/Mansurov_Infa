import heapq

def dijkstra(n, edges, start, end):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    pq = [(0, start)]
    distances = [float('inf')] * n
    distances[start] = 0
    parents = [-1] * n

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parents[current]
    path.reverse()

    return len(path), distances[end]


n, m, s, f = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

path_length, path_distance = dijkstra(n, edges, s, f)

print(path_length)