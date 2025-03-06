import math
import heapq

def calculate_distance(stone1, stone2):
    return math.sqrt((stone1[0] - stone2[0]) ** 2 + (stone1[1] - stone2[1]) ** 2)

def frog_distance(stones):
    n = len(stones)
    distances = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = calculate_distance(stones[i], stones[j])
            distances[i][j] = dist
            distances[j][i] = dist
    
    min_jump = [float('inf')] * n
    min_jump[0] = 0
    pq = [(0, 0)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        for v in range(n):
            if u != v:
                max_jump = max(current_dist, distances[u][v])
                if max_jump < min_jump[v]:
                    min_jump[v] = max_jump
                    heapq.heappush(pq, (max_jump, v))
    
    return min_jump[1]

def main():
    n = int(input())
    stones = []
    for _ in range(n):
        x, y = map(int, input().split())
        stones.append((x, y))
    
    result = frog_distance(stones)
    print(f"{result:.3f}")

main()