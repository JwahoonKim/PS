import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i] = [0] + (list(map(int, input().split())))

for i in range(m):
    result = 0
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2 + 1):
        result += sum(graph[x][y1 : y2 + 1])
    print(result)