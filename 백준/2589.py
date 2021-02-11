import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e5)
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(graph, x,  y):
    result = 0
    distance = [[INF] * col for _ in range(row)]
    q = deque()
    q.append((x, y))
    distance[x][y] = 0
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if graph[nx][ny] == 'L' and distance[nx][ny] == INF:
                    q.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1
                    result = max(distance[nx][ny], result)
    return result
            
            
if __name__ == "__main__":
    row, col = map(int, input().split())
    graph = []
    answer = 0
    for i in range(row):
        graph.append(list(map(str, input().rstrip())))
    
    for x in range(row):
        for y in range(col):
            if graph[x][y] == 'L':
                answer = max(answer, bfs(graph, x, y))
    print(answer)
   