from collections import deque
import sys

input = sys.stdin.readline
INF = int(1e9)

city, road, desti, start = map(int, input().split())
graph = [[] * (city + 1) for _ in range(city + 1)]
distance = [INF] * (city + 1)
for _ in range(road):
    a, b = map(int, input().split())
    graph[a].append(b)

distance[start] = 0
q = deque()
q.append(start)
while q:
    now = q.popleft()
    for i in graph[now]:
        if distance[i] == INF:
            distance[i] = distance[now] + 1
            q.append(i)            

check = False
for i in range(1, city + 1):
    if distance[i] == desti:
        print(i)
        check = True
if check == False:
    print(-1)