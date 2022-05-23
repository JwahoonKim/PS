import sys, heapq
input = sys.stdin.readline
INF = int(1e9) # sys.maxsize 라는 함수 사용가능 -> -INF 는 최솟값으로 사용가능

node, line = map(int, input().split())
graph = [[] for _ in range(node + 1)]
for _ in range(line):
    a, b, c =  map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (node + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

one_v1 = dijkstra(1)[v1]
one_v2 = dijkstra(1)[v2]
v1_v2 = dijkstra(v1)[v2]
v1_dest = dijkstra(v1)[node]
v2_dest = dijkstra(v2)[node]

if one_v1 + v2_dest < one_v2 + v1_dest:
    first = one_v1
    second = v1_v2
    dest = v2_dest
else:
    first = one_v2
    second = v1_v2
    dest = v1_dest

if first == INF or second == INF or dest == INF:
    print(-1)
else:
    print(first + second + dest)