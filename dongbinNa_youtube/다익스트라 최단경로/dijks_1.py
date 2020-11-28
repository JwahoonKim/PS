import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c  = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0    
    while q:
        now, dist = heapq.heappop(q)
        #방문한 적 있나 체크
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

dijkstra(c)
print(distance)
ans = 0 
count = 0
for d in distance:
    if d != INF:
        count += 1
        ans = max(ans, d)
    
print(count - 1, ans)