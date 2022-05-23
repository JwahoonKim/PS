from collections import deque

M, N = map(int, input().split())
box = []
q = deque()
for i in range(N):
    box.append(list(map(int, input().split())))

# 처음 익은 토마토 위치 큐에 삽입
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))

def bfs(M, N, box):
    day = -1
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while(q):
        day += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if box[nx][ny] == 0:
                        box[nx][ny] = 1
                        q.append((nx, ny))
    for row in box:
        if 0 in row:
            return -1
    return day

answer = bfs(M, N, box)
print(answer)

