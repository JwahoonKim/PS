from collections import deque

INF = int(1e9)
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

distance = [[[0] * 2 for _ in range(m)] for _ in range(n)]
distance[0][0][0] = 1

q = deque()
q.append((0, 0, 0))
while q:
    r, c, crushed = q.popleft()

    if r == n - 1 and c == m - 1:
        break

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if not (0 <= nr < n and 0 <= nc < m):
            continue

        if graph[nr][nc] == 1 and not crushed and distance[nr][nc][1] == 0:
            distance[nr][nc][1] = distance[r][c][crushed] + 1
            q.append((nr, nc, 1))

        elif graph[nr][nc] == 0 and distance[nr][nc][crushed] == 0:
            distance[nr][nc][crushed] = distance[r][c][crushed] + 1
            q.append((nr, nc, crushed))


if distance[n - 1][m - 1][0] == 0 and distance[n - 1][m - 1][1] == 0:
    print(-1)
elif distance[n - 1][m - 1][0] == 0:
    print(distance[n - 1][m - 1][1])
elif distance[n - 1][m - 1][1] == 0:
    print(distance[n - 1][m - 1][0])
else:
    print(min(distance[n - 1][m - 1][0], distance[n - 1][m - 1][1]))
