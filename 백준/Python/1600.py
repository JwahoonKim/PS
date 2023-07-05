from collections import deque

INF = int(1e9)
K = int(input())
W, H = map(int, input().split())

graph = []
for _ in range(H):
    graph.append(list(map(int, input().split())))

answer = INF

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
drh = [-1, -2, -2, -1, 1, 2, 2, 1]
dch = [-2, -1, 1, 2, 2, 1, -1, -2]

visited = [[[False] * W for _ in range(H)] for _ in range(K + 1)]

q = deque()
q.append((0, 0, K, 0))

while q:
    r, c, remain_k, move_cnt = q.popleft()
    if r == H - 1 and c == W - 1:
        answer = move_cnt
        break

    if remain_k >= 1:
        for i in range(8):
            nr = r + drh[i]
            nc = c + dch[i]
            if 0 <= nr < H and 0 <= nc < W:
                if not visited[remain_k - 1][nr][nc] and graph[nr][nc] == 0:
                    q.append((nr, nc, remain_k - 1, move_cnt + 1))
                    visited[remain_k - 1][nr][nc] = True

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < H and 0 <= nc < W:
            if not visited[remain_k][nr][nc] and graph[nr][nc] == 0:
                q.append((nr, nc, remain_k, move_cnt + 1))
                visited[remain_k][nr][nc] = True

answer = -1 if answer == INF else answer
print(answer)
