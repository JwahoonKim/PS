T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    count = 0
    check = 0
    flag = 0
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    for i in range(N):
        for _ in range(K):
            graph[i].append(0)
    for i in range(K):
        graph.append([0] * (N + K))
    #세로
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                for k in range(K):
                    if graph[i + k][j] == 0:
                        check = 0
                        break
                    if graph[i + k][j] == 1:
                        check += 1
                if check == K and graph[i + K][j] == 0 :
                    count += 1
                    check = 0
    #가로
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                for k in range(K):
                    if graph[i][j + k] == 0:
                        check = 0
                        break
                    if graph[i][j + k] == 1:
                        check += 1
                if check == K and graph[i][j + K] == 0:
                    count += 1
                    check = 0

    print(f'#{test_case} {count}')