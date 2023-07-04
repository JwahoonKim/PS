import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())

visited = [[[False] * m for _ in range(n)] for _ in range(h)]
graph = [[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        line = list(map(int, input().split()))
        graph[i].append(line)

dr = [0, 0, 0, 0, 1, -1]
dc = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k, 0))
                visited[i][j][k] = True

answer = 0
while q:
    z, r, c, day = q.popleft()
    answer = max(answer, day)
    graph[z][r][c] = 1

    for i in range(6):
        nr = r + dr[i]
        nc = c + dc[i]
        nz = z + dz[i]

        if 0 <= nr < n and 0 <= nc < m and 0 <= nz < h:
            if not visited[nz][nr][nc] and graph[nz][nr][nc] == 0:
                q.append((nz, nr, nc, day + 1))
                visited[nz][nr][nc] = True


def reaped_all_tomatoes():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    return False
    return True


if not reaped_all_tomatoes():
    print(-1)
else:
    print(answer)
