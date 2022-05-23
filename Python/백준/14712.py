n, m = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
count = 0

def dfs(x, y):
    global count
    # 종료 조건
    if (x, y) == (1, n + 1):
        count += 1
        return
    
    if x == m:
        nx, ny = 1, y + 1
    else:
        nx, ny = x + 1, y
        
    # x, y에 네모를 놓지 않은 경우
    dfs(nx, ny)
    
    # x, y에 네모를 놓을 수 있고 놓는 경우
    if graph[y - 1][x] == 0 or graph[y - 1][x - 1] == 0 or graph[y][x - 1] == 0:
        graph[y][x] = 1
        dfs(nx, ny)
        graph[y][x] = 0
        
dfs(1, 1)

print(count)
