from heapq import heappush
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

city = int(input())
bus = int(input())
graph = [[] for _ in range(city + 1)]
distance = [INF] * (city + 1)

for _ in range(bus):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, desti = map(int, input().split())

q = []
distance[start] = 0
heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = distance[now] + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

if distance[desti] != INF:
    print(distance[desti])