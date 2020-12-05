T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = []
    count = 0
    for i in range(N):
        graph.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(N):
            for k in range(M):
                #가로 체크
                if graph[i][j] != 0:
                    if j + M - 1 < N and ( j + M == N or graph[i][j + M] == 0):
                        for l in range(M):
                            if graph[i][j + l] != 1:
                                break
                            count += 1
                if graph[i][j] != 0:
                    if i + M - 1 < N and ( i + M == N or graph[i + M][j] == 0):
                        for m in range(M):
                            if graph[i + m][j] == 1:
                                break
                            count += 1
    print(f'#{test_case} {count}')