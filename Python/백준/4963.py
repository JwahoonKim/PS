import sys
sys.setrecursionlimit(100000)

def dfs(graph, x, y, w, h):
    if 0 <= x < w and 0 <= y < h:
        if graph[y][x] == 1:
            if visited[y][x] == False:   
                visited[y][x] = True
                for i in range(9):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    dfs(graph, nx, ny, w, h)
                return True
    return False

dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]

while(1):
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    count = 0
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    visited = [[False] * w for _ in range(h)]
    for x in range(w):
        for y in range(h):
            if dfs(graph, x, y, w, h) == True:
                count += 1
    print(count)