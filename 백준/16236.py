from collections import deque
import sys
import copy

input = sys.stdin.readline

INF = int(1e9)

# 먹을 수 있는 먹이 좌표 구하기
def find(size):
    feed = deque()
    for i in range(n):
        for j in range(n):
            if 0 < arr[i][j] < size:
                feed.append((i, j))
    return feed


# bfs로 최소경로 구하는 함수
def go(now, size):
    distance = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()

    for i in range(n):
        distance.append([INF] * n)

    x, y = now[0], now[1]
    q.append((x, y))
    distance[x][y] = 0
    
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if 0 <= arr[nx][ny] <= size:
                    if distance[nx][ny] == INF:
                        distance[nx][ny] = distance[x][y] + 1
                        q.append((nx, ny))
    return distance

if __name__ == "__main__":
    arr = []
    count = 0
    second = 0
    size = 2
    n = int(input())
    for i in range(n):
        arr.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                now = (i, j)
                arr[i][j] = 0
    distance = go(now, size)

    while(1):
        dist = INF
        feed = find(size)
        distance = go(now, size)
        if len(feed) == 0:
            break
        for i in feed:
            x, y = i[0], i[1]
            if distance[x][y] < dist:
                dist = distance[x][y]
                target = (x, y)
        if dist == INF:
            break

        arr[target[0]][target[1]] = 0
        now = target
        count += 1
        second += dist
        if count == size:
            size += 1
            count = 0
    print(second)    
