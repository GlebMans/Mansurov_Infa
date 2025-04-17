from collections import deque

def min_operations(N, M):
    queue = deque([(N, 0)])  # Queue stores tuples of (current number, steps)
    visited = set()  # To avoid revisiting numbers

    while queue:
        current, steps = queue.popleft()

        # If we reach M, return the number of steps
        if current == M:
            return steps

        # Mark the current number as visited
        if current in visited:
            continue
        visited.add(current)

        # Generate possible next states and add them to the queue
        if current - 2 >= 1 and (current - 2) not in visited:  # Decrease by 2
            queue.append((current - 2, steps + 1))
        if current * 3 <= 9999 and (current * 3) not in visited:  # Multiply by 3
            queue.append((current * 3, steps + 1))
        if current + sum(map(int, str(current))) <= 9999 and (current + sum(map(int, str(current)))) not in visited:  # Add sum of digits
            queue.append((current + sum(map(int, str(current))), steps + 1))

    # If no solution is found (shouldn't happen with valid inputs)
    return -1

# Input reading
N, M = map(int, input().split())
print(min_operations(N, M))