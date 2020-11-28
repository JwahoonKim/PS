#플로이드 워셜 알고리즘

INF = 987654321
n, m = map(int, input().split())
graph = [[INF]*(n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])


if graph[1][x] + graph[1][k] >= INF:
    ans = -1
else: ans = graph[1][x] + graph[x][k]

print(ans)

