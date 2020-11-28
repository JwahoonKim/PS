#heap을 사용하여 시간복잡도를 낮추는 방법
import heapq
import sys
from sys import displayhook
input = sys.stdin.readlines
INF = 987654321

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # (거리, 노드)
    distance[start] = 0 
    while q:
        dist , now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost, i[0]))

dijkstra(start)