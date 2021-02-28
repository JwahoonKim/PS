def solution(n, s, a, b, fares):
    minCost = 9876543210

    graph = [[9876543210] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        graph[i][i] = 0

    for start, end, cost in fares:
        graph[start][end] = cost
        graph[end][start] = cost

    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                # graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])
                # 위에랑 아래랑 시간차이 두배나는데 뭐지
                if graph[x][y] > graph[x][k] + graph[k][y]:
                    graph[x][y] = graph[x][k] + graph[k][y]

    for k in range(1, n + 1):
        cost = graph[s][k] + graph[k][a] + graph[k][b]
        minCost = min(minCost, cost)

    return minCost


n = 6
s = 4
a = 6
b = 2
fares = [
    [4, 1, 10],
    [3, 5, 24],
    [5, 6, 2],
    [3, 1, 41],
    [5, 1, 24],
    [4, 6, 50],
    [2, 4, 66],
    [2, 3, 22],
    [1, 6, 25],
]

print(solution(n, s, a, b, fares))
