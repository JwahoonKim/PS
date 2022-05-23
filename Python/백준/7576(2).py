from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

m, n = map(int, input().split())
box = []
for _ in range(n):
    box.append(list(map(int, input().split())))

q = deque()
# 처음 익어있는 토마토 정보 큐에 삽입
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))

day = -1
while q:
    day += 1
    for _ in range(len(q)):
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n: # 박스 범위 안에서
                if box[ny][nx] == 0: # 안익은 토마토라면
                    box[ny][nx] = 1
                    q.append((ny, nx))

for line in box:
    if 0 in line:
        day = -1
        break

print(day)