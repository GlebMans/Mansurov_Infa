def bellman_ford(n, wormholes):
    dist = [float('inf')] * n
    dist[0] = 0
    
    for _ in range(n-1):
        for x, y, t in wormholes:
            if dist[x] != float('inf') and dist[x] + t < dist[y]:
                dist[y] = dist[x] + t
    
    for x, y, t in wormholes:
        if dist[x] != float('inf') and dist[x] + t < dist[y]:
            return True
    
    return False

def solve():
    c = int(input())
    results = []
    
    for _ in range(c):
        n, m = map(int, input().split())
        wormholes = []
        for _ in range(m):
            x, y, t = map(int, input().split())
            wormholes.append((x, y, t))
        
        if bellman_ford(n, wormholes):
            results.append("Возможно")
        else:
            results.append("Не возможно")
    
    for result in results:
        print(result)

solve()