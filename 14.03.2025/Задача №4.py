import sys
import heapq

def minimum_total_distance(N, M, district_centers, roads):
    graph = {i: [] for i in range(N)}
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))

    INF = float('inf')
    min_distance = [INF] * N
    min_heap = []

    for center in district_centers:
        min_distance[center] = 0
        heapq.heappush(min_heap, (0, center))

    while min_heap:
        current_dist, node = heapq.heappop(min_heap)
        
        if current_dist > min_distance[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < min_distance[neighbor]:
                min_distance[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    total_distance = sum(min_distance[i] for i in range(N) if i not in district_centers and min_distance[i] != INF)

    return total_distance

data = list(map(int, sys.stdin.readline().split()))
N, M = data[0], data[1]
district_centers = set(data[2:])

roads = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

result = minimum_total_distance(N, M, district_centers, roads)
print(result)
