import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
    if 0 <= x < N and 0 <= y < M:
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x - 1, y)      
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
        else:
            return False
    return False

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    count = 0
    graph = [[0] * M for _ in range(N)]
    for i in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                count += 1
    print(count)