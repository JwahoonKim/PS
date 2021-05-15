# 섬마다 좌표를 찾아서 
# 서로 다른 섬의 좌표끼리 거리가 최소인 경우 구해

from collections import deque

def bfs(n):
    global landNumber
    visited = [[False] * n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if visited[i][j] == True or graph[i][j] == 0:
                continue
            landNumber += 1
            q.append((i, j))
            while(q):
                x, y = q.pop()
                landInfo.append([(x, y), landNumber])
                visited[x][y] = True
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] == 1 and visited[nx][ny] == False:
                            q.append((nx, ny))     

n = int(input())
landNumber = 0
graph = [list(map(int, input().split())) for _ in range(n)]
landInfo = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
bfs(n)
answer = 100000
for land1 in landInfo:
    for land2 in landInfo:
        x1, y1, num1 = land1[0][0], land1[0][1], land1[1]
        x2, y2, num2 = land2[0][0], land2[0][1], land2[1]
        if num1 != num2:
            dist = abs(x1 - x2) + abs(y1 - y2) - 1
            answer = min(dist, answer)
print(answer)