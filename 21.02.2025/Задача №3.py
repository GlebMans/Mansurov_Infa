def max_meetings(start, end, n):
    meetings = [(start[i], end[i]) for i in range(n)]
    
    meetings.sort(key=lambda x: x[1])
    
    count = 0
    last_end_time = -1
    
    for s, e in meetings:
        if s > last_end_time:
            count += 1
            last_end_time = e
    
    return count


n = int(input())
start = list(map(int, input().split()))
end = list(map(int, input().split()))

result = max_meetings(start, end, n)

print(result)