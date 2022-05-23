import sys, copy

input = sys.stdin.readline

# 확산과정을 표현하는 함수
def diffusion(arr):
    row = len(arr)
    col = len(arr[0])
    # 0이 아닌 곳(미세먼지가 있는 곳)을 찾아서 그 점 기준으로 확산시키기
    nonZeroCheck = [[False] * col for _ in range(row)]
    afterDiffusion = copy.deepcopy(arr)
    for i in range(row):
        for j in range(col):
            if arr[i][j] > 0:
                nonZeroCheck[i][j] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(row):
        for y in range(col):
            if nonZeroCheck[x][y] == False:
                continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if arr[nx][ny] >= 0:
                    afterDiffusion[x][y] -= arr[x][y] // 5
                    afterDiffusion[nx][ny] += arr[x][y] // 5
    return afterDiffusion


def airClean(arr):
    row = len(arr)
    col = len(arr[0])
    # 공기청정기 위치 찾기, upper --> 공기청정기 위쪽 좌표
    upper = 0
    for i in range(row):
        if arr[i][1] == -1:
            upper = i
            break
    lower = upper + 1
    direction = 0
    # start point
    x, y = upper - 1, 1
    # 위쪽 공기청정기 작동
    for i in range(upper - 1, 1, -1):
        arr[i][1] = arr[i - 1][1]
    for i in range(1, col - 1):
        arr[1][i] = arr[1][i + 1]
    for i in range(1, upper):
        arr[i][col - 2] = arr[i + 1][col - 2]
    for i in range(col - 2, 1, -1):
        arr[upper][i] = arr[upper][i - 1]
    arr[upper][2] = 0

    # 아래쪽 공기청정기 작동
    for i in range(lower + 1, row - 1):
        arr[i][1] = arr[i + 1][1]
    for i in range(1, col - 1):
        arr[row - 2][i] = arr[row - 2][i + 1]
    for i in range(row - 1, lower, -1):
        arr[i][col - 2] = arr[i - 1][col - 2]
    for i in range(col - 2, 2, -1):
        arr[lower][i] = arr[lower][i - 1]
    arr[lower][2] = 0
    return arr


if __name__ == "__main__":
    row, col, T = map(int, input().split())
    graph = [[] for _ in range(row + 2)]
    # 테두리를 -2로 설정
    graph[0] = [-2] * (col + 2)
    graph[row + 1] = [-2] * (col + 2)
    for i in range(1, row + 1):
        graph[i] = [-2] + list(map(int, input().split())) + [-2]
    # T초 지난 후 --> T번 확산 + 공기청정
    for _ in range(T):
        graph = airClean(diffusion(graph))
    # graph에서 양수인 곳만 더하면 답
    answer = 0
    for i in range(row + 1):
        for j in range(col + 1):
            if graph[i][j] >= 0:
                answer += graph[i][j]
    # 정답 출력
    print(answer)
