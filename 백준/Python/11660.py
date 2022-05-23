import sys, copy

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
sumGraph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i] = [0] + (list(map(int, input().split())))

# sumGraph를 O(N^2)으로 만드는 과정
sumGraph[1][1] = graph[1][1]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        sumGraph[i][j] = (
            graph[i][j]
            + sumGraph[i - 1][j]
            + sumGraph[i][j - 1]
            - sumGraph[i - 1][j - 1]
        )

# 답 m번 구하기
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 이런 방식으로 구해야 M이 아무리 커도 O(1) 복잡도로 답을 구할 수 있다.
    ans = (
        sumGraph[x2][y2]
        - sumGraph[x2][y1 - 1]
        - sumGraph[x1 - 1][y2]
        + sumGraph[x1 - 1][y1 - 1]
    )
    print(ans)