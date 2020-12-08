T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    graph = []
    graph_90  = [[0] * (N) for _ in range(N)]
    graph_180 = [[0] * (N) for _ in range(N)]
    graph_270 = [[0] * (N) for _ in range(N)]
    for i in range(N):
        graph.append(list(map(int, input().split())))
    print(f'#{test_case}')
    for i in range(N): 
        for j in range(N - 1, -1, -1):
            graph_90[i][N - 1 - j] = graph[j][i]
    for i in range(N): 
        for j in range(N - 1, -1, -1):
            graph_180[i][N - 1 - j] = graph_90[j][i]
    for i in range(N): 
        for j in range(N - 1, -1, -1):
            graph_270[i][N - 1 - j] = graph_180[j][i]
    for i in range(N):
        for j in range(N):
            print(graph_90[i][j], end = "")
        print(' ', end ="")
        for j in range(N):
            print(graph_180[i][j], end = "")
        print(' ', end ="")
        for j in range(N):
            print(graph_270[i][j], end = "")
        print('')
     

