# 되돌아오는 경로를 생각하지 못해서 시간이 좀 걸렸음
# 코드 치기전에 문제 생각 좀 더 하고 시작하자
# visited를 set으로 바꾸면 좀 더 빠르게 할 수 있을 듯

visited = []


def move(type, x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    i = 0
    if type == 'U':
        i = 0
    elif type == 'D':
        i = 1
    elif type == 'L':
        i = 2
    else:
        i = 3
    nx, ny = x + dx[i], y + dy[i]
    if nx < -5 or nx > 5 or ny > 5 or ny < -5:
        return [False, x, y]
    if [x, y, nx, ny] in visited or [nx, ny, x, y] in visited:
        return [False, nx, ny]
    visited.append([x, y, nx, ny])
    return [True, nx, ny]


def solution(dirs):
    answer = 0
    dirs = list(dirs)
    x, y = 0, 0
    for _dir in dirs:
        _bool, x, y = move(_dir, x, y)
        if _bool:
            answer += 1
    return answer
