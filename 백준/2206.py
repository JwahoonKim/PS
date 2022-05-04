from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dist_without_crash = [[-1] * m for _ in range(n)]
dist_with_crash = [[-1] * m for _ in range(n)]
dist_without_crash[0][0] = 1
dist_with_crash[0][0] = 1

q = deque()
q.append((0, 0, False)) # (x, y, 벽 뚫어본 여부)

while q:
    x, y, crashed = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and (nx, ny) != (0, 0):
            if graph[nx][ny] == 1 and not crashed:
                dist_with_crash[nx][ny] = dist_without_crash[x][y] + 1
                q.append((nx, ny, True))
            elif graph[nx][ny] == 0 and not crashed and dist_without_crash[nx][ny] == -1:
                dist_without_crash[nx][ny] = dist_without_crash[x][y] + 1
                q.append((nx, ny, False))
            elif graph[nx][ny] == 0 and crashed and dist_with_crash[nx][ny] == -1:
                dist_with_crash[nx][ny] = dist_with_crash[x][y] + 1
                q.append((nx, ny, True))

if dist_with_crash[-1][-1] == -1 and dist_without_crash[-1][-1] == -1:
    print(-1)
elif dist_with_crash[-1][-1] != -1 and dist_without_crash[-1][-1] != -1:
    print(min(dist_without_crash[-1][-1], dist_with_crash[-1][-1]))
else:
    print(max(dist_without_crash[-1][-1], dist_with_crash[-1][-1]))