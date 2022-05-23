def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for start, dest, fare in fares:
        graph[start][dest] = fare
        graph[dest][start] = fare
    
    for i in range(1, n + 1):
        graph[i][i] = 0

    # 플로이드 워셜 알고리즘
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, n + 1):
        cost = graph[s][i] + graph[i][a] + graph[i][b]
        answer = min(answer, cost)    

    return answer