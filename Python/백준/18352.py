from collections import deque
import sys

input = sys.stdin.readline

INF = int(1e9)

# 입력 받기
n, m, k, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append([start, 0])

visited = [False] * (n + 1)
distance = [INF] * (n + 1)
distance[start] = 0

# BFS
while q:
    now, dist = q.popleft()
    if visited[now] == False:
        visited[now] = True
        distance[now] = dist
        for next in graph[now]:
            q.append([next, dist + 1])

# 출력
if k not in distance:
    print(-1)
else:
    for i in range(1, n + 1):
        if distance[i] == k:
            print(i)
