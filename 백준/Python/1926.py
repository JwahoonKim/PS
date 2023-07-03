import sys
sys.setrecursionlimit(int(1e9))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

picture_cnt = 0
answer = 0

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]


def dfs(r, c, visited):
    visited[r][c] = True
    result = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if not visited[nr][nc] and graph[nr][nc] == 1:
                result += dfs(nr, nc, visited)

    return result


for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            picture_cnt += 1
            result = dfs(i, j, visited)
            answer = max(answer, result)

print(picture_cnt)
print(answer)
