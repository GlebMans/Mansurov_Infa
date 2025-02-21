from collections import deque

def knight_directions(n, start_x, start_y):
    directions = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    board = [[-1 for _ in range(n)] for _ in range(n)]

    queue = deque([(start_x, start_y, 0)])  # (x, y, steps)
    board[start_x][start_y] = 0
    
    while queue:
        x, y, steps = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
                board[nx][ny] = steps + 1
                queue.append((nx, ny, steps + 1))
    
    return board


n = 9
start_x, start_y = 4, 4
result = knight_directions(n, start_x, start_y)
for row in result:
    print(row)