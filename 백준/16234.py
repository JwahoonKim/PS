import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, graph):
    if 0 <= x < n and 0 <= y < n:
        if visited[x][y] == False:
            visited[x][y] = True
            stack.append((x, y))
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if lower <= abs(graph[nx][ny] - graph[x][y]) <= upper:
                        dfs(nx, ny, graph)
            return True
        return False
    return False


# 입력받기
n, lower, upper = map(int, input().split())
answer = 0
stack = []
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False] * n for _ in range(n)]
unions = []

while 1:
    for i in range(n):
        for j in range(n):
            if dfs(i, j, graph) == True:
                # union이 형성되면 연합국들 모임을 unions에 append
                if len(stack) > 1:
                    unions.append(stack)
                stack = []
    if not unions:
        break
    else:
        answer += 1
        for union in unions:
            people = 0
            # 인구조사
            for nation in union:
                x, y = nation
                people += graph[x][y]
            # 인구 이동한 후 인구수
            result = people // len(union)
            # 인구 이동 적용
            for nation in union:
                x, y = nation
                graph[x][y] = result
    # reset
    unions = []
    visited = [[False] * n for _ in range(n)]
print(answer)
