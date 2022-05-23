import sys
import copy
input = sys.stdin.readline
# dfs 함수를 색깔별로 안하고 한꺼번에 할 수 있지 않을까


def dfsRed(x, y, arr):
    if arr[x][y] == 'R':
        arr[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                dfsRed(nx, ny, arr)
        return True
    return False


def dfsGreen(x, y, arr):
    if arr[x][y] == 'G':
        arr[x][y] = 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                dfsGreen(nx, ny, arr)
        return True
    return False


def dfsBlue(x, y, arr):
    if arr[x][y] == 'B':
        arr[x][y] = 3
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                dfsBlue(nx, ny, arr)
        return True
    return False


if __name__ == '__main__':
    n = int(input())
    color = []
    for i in range(n):
        color.append(list(map(str, input().rstrip())))

    # 적록색약용 그래프
    colorRB = copy.deepcopy(color)
    for i in range(n):
        for j in range(n):
            if colorRB[i][j] == 'G':
                colorRB[i][j] = 'R'

    areaRGB = 0
    areaRB = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 정상인용 dfs
    for i in range(n):
        for j in range(n):
            if dfsRed(i, j, color) == True:
                areaRGB += 1
            if dfsGreen(i, j, color) == True:
                areaRGB += 1
            if dfsBlue(i, j, color) == True:
                areaRGB += 1
    # 적록색약용 dfs
    for i in range(n):
        for j in range(n):
            if dfsRed(i, j, colorRB) == True:
                areaRB += 1
            if dfsBlue(i, j, colorRB) == True:
                areaRB += 1
    # 정답
    print(areaRGB, areaRB)
