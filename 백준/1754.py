import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

node, line = map(int, input().split())
start = int(input())
graph = [[] for _ in range(node + 1) ]
distance = [INF] * (node + 1)

for _ in range(line):
    u, v, w = map(int, input().split()) 
    graph[u].append((v, w))

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = distance[now] + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
    
for i in range(1, node + 1):
    if distance[i] == INF:
        print("INF")
    else: print(distance[i])