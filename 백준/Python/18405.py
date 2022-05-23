from collections import deque

# 1초 동안 감염시키는 함수
def infection(graph, que):
    nextque = deque()
    while(q):
        virus, (x, y) = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    nextque.append([virus, (nx, ny)])
    return deque(sorted(nextque))

# 정보 받기
n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
s, a, b = map(int, input().split())
q = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 초기 바이러스 번호순대로 큐에 삽입
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            q.append([graph[i][j], (i, j)])
# 번호순 정렬
q = deque(sorted(q))
# 큐에 입력된대로 번식 + 큐 삽입 반복
for _ in range(s):
    q = infection(graph, q)

print(graph[a - 1][b - 1])

