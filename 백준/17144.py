import sys

input = sys.stdin.readline

# 특정 지점에서 확산될 공간이 몇개 있는지 확인하는 함수
def countNoWall(graph, x, y):
    count = 4
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if graph[nx][ny] < 0:
            count -= 1
    return count


# 확산과정을 표현하는 함수
def diffusion(graph):
    row = len(graph)
    col = len(graph[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(row):
        for y in range(col):
            if graph[x][y] >= 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if graph[nx][ny] >= 0:
                        graph[nx][ny] += graph[x][y] // 5
                        graph[x][y] -= graph[x][y] // 5
    return graph


def airClean(graph):
    row = len(graph)
    col = len(graph[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    # 공기청정기 위치 찾기
    upper = 0
    for i in range(row):
        if graph[i][0] == -1:
            upper = i
            break
    lower = upper + 1
    # 첫줄에서 위쪽으로
    for i in range(upper - 1, 1):
        graph[i][0] = graph[i - 1][0]
    # 맨위에서 우측으로
    for i in range(1, col - 2):
        graph[1][i] = graph[1][i + 1]
    # 맨위 & 맨오른쪽에서 아래로
    for i in range(1, upper):
        graph[i + 1][col - 1] = graph[i][col - 1]
    # 맨 오른쪽 & 맨아래에서 왼쪽으로
    for i in range(col - 2, 1):
        graph[upper][i] = graph[upper][i - 1]
    # 아래쪽 시계방향 청정
    for j in range(lower - 1, row - 1):
        graph[j][1] = graph[j + 1][1]
    for j in range(2, col):
        graph[row - 1][j - 1] = graph[row - 1][j]
    for j in range(row - 2, lower):
        graph[j][col - 2] = graph[j - 1][col - 2]
    for j in range(col - 2, 1):
        graph[lower][i] = graph[lower][i - 1]
    return graph


row, col, T = map(int, input().split())
graph = [[] for _ in range(row + 2)]
# 테두리를 -2로 설정
graph[0] = [-2] * (col + 2)
graph[row + 1] = [-2] * (col + 2)
for i in range(1, row + 1):
    graph[i] = [-2] + list(map(int, input().split())) + [-2]

graph = diffusion(graph)
print('')
for i in range(1, len(graph) - 1):
    for j in range(1, col + 1):
        print(graph[i][j], end = ' ')
    print('')
graph = airClean(graph)
print('')
for i in graph:
    print(i) 