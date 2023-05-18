from collections import deque


def in_board(r, c):
    if 0 <= r < n and 0 <= c < m:
        return True
    return False


def bfs():
    while q:
        r1, c1, r2, c2, cnt = q.popleft()

        if cnt >= 10:
            return -1

        for i in range(4):
            nr1 = r1 + dr[i]
            nr2 = r2 + dr[i]
            nc1 = c1 + dc[i]
            nc2 = c2 + dc[i]

            if in_board(nr1, nc1) and in_board(nr2, nc2):
                if graph[nr1][nc1] == '#':
                    nr1, nc1 = r1, c1
                if graph[nr2][nc2] == '#':
                    nr2, nc2 = r2, c2
                q.append((nr1, nc1, nr2, nc2, cnt + 1))

            elif not in_board(nr1, nc1) and not in_board(nr2, nc2):
                continue
            else:
                return cnt + 1


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(input()))

r1, c1 = -1, -1
r2, c2 = -1, -1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'o':
            r1, c1 = i, j
            break

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'o' and (r1, c1) != (i, j):
            r2, c2 = i, j
            break

q = deque()
q.append((r1, c1, r2, c2, 0))
print(bfs())
