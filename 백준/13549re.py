import sys
from collections import deque 

n, k = map(int, input().split())

visited = [-1] * 2000002
q = deque()
q.append((n, 0))
visited[n] = 0

while(q):
    x, time = q.popleft()
    if visited[x] == -1:
        visited[x] = time
    if x == k:
        print(visited[x])
        break
    if x <= 100000 and visited[2 * x] == -1:
        q.appendleft((2 * x, time))
    # -1칸 하는 작업
    if x >= 1 and visited[x - 1] == -1:
        q.append((x - 1, time + 1))
    # +1칸 하는 작업
    if x < 100001 and visited[x + 1] == -1:
        q.append((x + 1, time + 1))
    

