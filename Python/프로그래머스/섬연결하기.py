from collections import deque


def findOtherRoute(n, start, end, graph):
    q = deque()
    q.append(start)
    visited = [False] * n
    while q:
        now = q.popleft()
        visited[now] = True
        if now == end:
            return True
        for next in range(n):
            if graph[now][next] != -1 and visited[next] == False:
                # start -- > end로 바로 가는 경우는 안됨
                if now == start and next == end:
                    continue
                q.append(next)
    return False


def solution(n, costs):
    answer = 0
    graph = [[-1] * n for _ in range(n)]

    for a, b, cost in costs:
        graph[a][b] = cost
        graph[b][a] = cost

    # 비용이 큰 다리부터 없애보자
    costs = sorted(costs, key=lambda x: x[2], reverse=True)
    for i in range(len(costs)):
        start, end, cost = costs[i]
        # start -- > end로 가는 직통말고 다른 길이 있다면 다리 없애
        if findOtherRoute(n, start, end, graph) == True:
            costs[i][2] = -1
            graph[start][end] = -1
            graph[end][start] = -1

    for a, b, cost in costs:
        if cost != -1:
            answer += cost

    return answer
