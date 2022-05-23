# BFS를 사용하여 최단경로를 찾는다.

from collections import deque

INF = int(1e9)
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    graph = []
    graph_check = [[INF] * N for _ in range(N)]
    for i in range(N):
        graph.append(list(map(int, input())))
    q = deque()
    q.append((0, 0))
    graph_check[0][0] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph_check[nx][ny] > graph[nx][ny] + graph_check[x][y]:
                    graph_check[nx][ny] = graph[nx][ny] + graph_check[x][y]
                    q.append((nx, ny))
    print(f'#{test_case} {graph_check[N - 1][N - 1]}')

