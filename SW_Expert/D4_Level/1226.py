# global 변수 쓸 생각을 못해서 오래 걸린 문제
# DFS , BFS 둘 중 하나로 풀면 될 것같다.
def dfs(x, y):
    global ans
    N = 16
    if 0 <= x < N and 0 <= y < N:
        if graph[x][y] == 3 or ans == 1:
            ans = 1
            return
        elif graph[x][y] == 1 or ans == 1:
            return
        elif graph[x][y] == 0 or ans == 1:
            graph[x][y] = 1
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
T = 10
for test_case in range(1, T + 1):
    ans = 0
    N = int(input())
    graph = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        if 2 in graph[i]:
            y = graph[i].index(2)
            x, y = i, y
            break
    graph[x][y] = 0
    dfs(x, y)
    print(f'#{test_case} {ans}')

# BFS
'''
from collections import deque 
move_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
 
def bfs():
    queue = deque()
    queue.append((1, 1))
    map_list[1][1] = 1
    while len(queue):
        y, x = queue.popleft()
        if map_list[y][x] == 3:
            return 1
        map_list[y][x] = 1
        for i in move_list:
            my = i[0] + y
            mx = i[1] + x
            if 0 <= my < N and 0 <= mx < N and map_list[my][mx] != 1:
                queue.append((my, mx))
    return 0
 
 
for _ in range(10):
    t = int(input())
    N = 16
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    #1,1 위치부터 탐색시작
    print('#{} {}'.format(t, bfs()))
'''