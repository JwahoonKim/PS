from collections import deque


def solution(maps):
    q = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    x_length = len(maps)
    y_length = len(maps[0])

    for i in range(x_length):
        for j in range(y_length):
            if maps[i][j] == 0:
                maps[i][j] = -1
    maps[0][0] = 1
    q.append([0, 0])
    while(q):
        x, y = q.popleft()
        dist = maps[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < x_length and 0 <= ny < y_length:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = dist + 1
                    q.append([nx, ny])
                elif maps[nx][ny] != -1:
                    if maps[nx][ny] > dist + 1:
                        maps[nx][ny] = dist + 1
                        q.append([nx, ny])
    return -1 if maps[x_length - 1][y_length - 1] == 1 else maps[x_length - 1][y_length - 1]
