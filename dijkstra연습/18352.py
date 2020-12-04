import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

node, edge, k, start = map(int, input().split())
graph = [[] for _ in range(node + 1)]
for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
distance = [INF] * (node + 1)

q = []
distance[start] = 0
heapq.heappush(q, (0, start))
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
if k not in distance:
    print(-1)
else:
    for i in range(1, len(distance)):
        if distance[i] == k:
            print(i)

