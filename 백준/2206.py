from collections import deque
import copy, sys
input = sys.stdin.readline

# 벽을 안깨고 최단경로를 찾는 함수
def bfs(graph):
    row = len(graph)
    col = len(graph[0])
    arr = [[0] * col for _ in range(row)]
    arr[0][0] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append((0,0))
    while(q):
        x, y = q.popleft()
        now = arr[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if graph[nx][ny] == 0:
                    if arr[nx][ny] == 0:
                        arr[nx][ny] = now + 1
                        q.append((nx, ny))
    return -1 if arr[nx][ny] == 0 else arr[row - 1][col - 1] 

n, m = map(int, input().split())
block = []
for i in range(n):
    block.append(list(map(int, input().rstrip())))
answer = 9999

for x in range(n):
    for y in range(m):
        temp = copy.deepcopy(block)
        if temp[x][y] == 1:
            temp[x][y] = 0 
            a = bfs(temp)
            if a >= 1:
                answer = min(answer, a)
print(answer if answer != 9999 else -1)

