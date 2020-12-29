# 큐 만드는 데 쓰이는 라이브러리 불러오기
from collections import deque 

#변수 받기
N,M = map(int, input().split())
graph = []
#방향 벡터 생성
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

#graph에 미로 만들기
for i in range(N):
    graph.append(list(map(int,input())))

#BFS를 사용 -> 큐를 생성
que = deque()

#미로문제 BFS로 
def BFS(x,y):
    que.append((x,y))
    while que:  # 큐가 빌때까지 반복
        x, y =  que.popleft()  #큐 꺼내오기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= N or ny <= -1 or ny >= M: #범위 벗어나는곳
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1    #한발자국 추가
                que.append((nx,ny))
    return graph[N-1][M-1]  #미로 끝지점 좌표값 리턴

print(BFS(0,0))