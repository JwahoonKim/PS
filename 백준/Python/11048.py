n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(1, n):
    graph[i][0] += graph[i - 1][0]

for i in range(1, m):
    graph[0][i] += graph[0][i - 1]

for i in range(1, n):
    for j in range(1, m):
        graph[i][j] += max(graph[i - 1][j], graph[i][j - 1])

print(graph[-1][-1])