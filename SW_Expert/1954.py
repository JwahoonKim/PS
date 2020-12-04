N = int(input())
graph = [[0] * N for _ in range(N)]
num = 1
x, y = 0, 0
dir = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(N * N):
    graph[x][y] = num
    num += 1
    x = x + dx[dir]
    y = y + dy[dir]
    if  x < 0 or x > N - 1 or y < 0 or y > N - 1 or graph[x][y] != 0:
        x = x - dx[dir]
        y = y - dy[dir]
        dir = (dir + 1) % 4
        x = x + dx[dir]
        y = y + dy[dir]

for i in range(N):
    for j in range(N):
        print(graph[i][j], end = " ")
    print("")
