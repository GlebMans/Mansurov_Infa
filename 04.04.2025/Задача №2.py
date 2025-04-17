def solve():
    t = int(input())
    for _ in range(t):
        # Read N
        N = int(input())
        # Read the N cards
        cards = []
        for _ in range(N):
            cards.append(int(input()))
        # Count the frequency of each card
        freq = {}
        for num in cards:
            freq[num] = freq.get(num, 0) + 1
        # Read the number of exchange types
        e = int(input())
        # Build the adjacency list for the graph
        graph = {}
        for _ in range(e):
            x, y = map(int, input().split())
            if x not in graph:
                graph[x] = []
            if y not in graph:
                graph[y] = []
            graph[x].append(y)
            graph[y].append(x)
        # Find all connected components using BFS
        visited = set()
        components = []
        for num in graph:
            if num not in visited:
                queue = [num]
                visited.add(num)
                component = []
                while queue:
                    current = queue.pop(0)
                    component.append(current)
                    for neighbor in graph.get(current, []):
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                components.append(component)
        # Determine which numbers are missing (deficit) and which are surplus
        surplus = {}
        deficit = []
        # Numbers that are present more than once are surplus
        for num in freq:
            if freq[num] > 1:
                surplus[num] = freq[num] - 1
        # Numbers from 1 to N not present in freq are deficit
        for num in range(1, N+1):
            if num not in freq:
                deficit.append(num)
        # Now, for each component, calculate the surplus and deficit within it
        total_swaps = 0
        for component in components:
            comp_surplus = 0
            comp_deficit = 0
            for num in component:
                if num in surplus:
                    comp_surplus += surplus[num]
                if num in deficit:
                    comp_deficit += 1
            # The number of swaps needed is the max of surplus or deficit in the component
            total_swaps += max(comp_surplus, comp_deficit)
        print(total_swaps)
        # Handle the blank line after each test case
        if _ < t - 1:
            input()

solve()