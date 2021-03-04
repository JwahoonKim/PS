from itertools import combinations as comb
import copy


def dfs(x, y, graph):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    if 0 <= x < n and 0 <= y < m:
        if graph[x][y] == 2:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = 2
                        dfs(nx, ny, graph)


def diffusion(graph):
    stack = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 2:
                dfs(x, y, graph)


def countZero(graph):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    return count


# 입력받기
n, m = map(int, input().split())
answer = 0
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


# 벽 세울수 있는 곳 찾기
canBuild = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            canBuild.append((i, j))

hubo = list(comb(canBuild, 3))

# 벽 세워보고 안전지대 개수 세어보기
for wall in hubo:
    tmp = copy.deepcopy(graph)
    x1, y1 = wall[0]
    x2, y2 = wall[1]
    x3, y3 = wall[2]
    tmp[x1][y1] = 1
    tmp[x2][y2] = 1
    tmp[x3][y3] = 1
    diffusion(tmp)
    answer = max(answer, countZero(tmp))

print(answer)
