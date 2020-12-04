T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    graph = [[0] * N for _ in range(N)]
    num = 1
    x, y = 0, 0
    dir = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(N * N):
        graph[x][y] = num
        num += 1
        x = x + dx[dir]
        y = y + dy[dir]
        if  x < 0 or x > N - 1 or y < 0 or y > N - 1 or graph[x][y] != 0:
            x = x - dx[dir]
            y = y - dy[dir]
            dir = (dir + 1) % 4
            x = x + dx[dir]
            y = y + dy[dir]
    print('#',test_case)
    for i in range(N):
        for j in range(N):
            print(graph[i][j], end = " ")
        print("")