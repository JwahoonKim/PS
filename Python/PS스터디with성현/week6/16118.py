import heapq, copy

INF = int(1e9)
start = 1
even = 2
odd = 1
node, edge = map(int, input().split())
graph_fox = [[] * (node  + 1) for _ in range(node + 1)]
distance_fox = [INF] * (node + 1)
distance_wolf = [INF] * (node + 1)
for _ in range(edge):
    a, b, c = map(int, input().split())
    graph_fox[a].append((b, c))
    graph_fox[b].append((a, c))
graph_wolf = copy.deepcopy(graph_fox)

#여우용 다익스트라
q = []
heapq.heappush(q, (0, start))
distance_fox[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if dist > distance_fox[now]:
        continue
    for i in graph_fox[now]:
        cost = distance_fox[now] + i[1]
        if cost < distance_fox[i[0]]:
            distance_fox[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

#늑대용 다익스트라
number = even
heapq.heappush(q, (0, start))
distance_wolf[start] = 0
while q:
    dist, now = heapq.heappop(q)   
    if dist > distance_wolf[now]:
        continue
    for i in graph_wolf[now]:
        if number == odd:
            cost = distance_wolf[now] + i[1] * 2
            if cost < distance_wolf[i[0]]:
                distance_wolf[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        if number == even:
            cost = distance_wolf[now] + i[1] / 2
            if cost < distance_wolf[i[0]]:
                distance_wolf[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                number = odd
    number = odd if number == even else even

print(distance_fox)
print(distance_wolf)
