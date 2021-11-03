from collections import deque

# 입력받기 및 변수 설정
n, m, v = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

# 간선 연결
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 그래프 연결상태 오름차순 정렬
for node in graph:
    node.sort()

# dfs
def dfs(start):
    visited_dfs[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if visited_dfs[i] == False:
            dfs(i)

# bfs
def bfs(start):
    q = deque()
    q.append(start)
    visited_bfs[start] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if visited_bfs[i] == False:
                q.append(i)
                visited_bfs[i] = True

# 함수 실행
dfs(v)
print("")
bfs(v)