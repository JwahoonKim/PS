import heapq


def solution(N, road, K):
    INF = int(1e9)
    answer = 0
    visited = [False] * (N + 1)
    distance = [INF] * (N + 1)
    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    for x, y, t in road:
        if t < graph[x][y]:
            graph[x][y] = t
            graph[y][x] = t

    q = [(0, 1)]
    distance[1] = 0
    while(q):
        dist, now = heapq.heappop(q)
        if visited[now] == True:
            continue
        visited[now] = True
        for i in range(1, N + 1):
            if visited[i] == False:
                if distance[i] > dist + graph[now][i]:
                    distance[i] = dist + graph[now][i]
                    heapq.heappush(q, (distance[i], i))
    for dist in distance:
        if dist <= K:
            answer += 1
    return answer
