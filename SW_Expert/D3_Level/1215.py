
T = 10

def hori_check(graph, N):
    #8 - N + 1 끼지 확인
    count = 0
    flag = 0
    for i in range(8):
        for j in range(9 - N):
            for k in range(N):
                if graph[i][j + k] != graph[i][N - 1 + j - k]:
                    break
                else: flag += 1
            if flag == N:
                count += 1
            flag = 0
    return count

def verti_check(graph, N):
    count = 0
    flag = 0
    for i in range(8):
        for j in range(9 - N):
            for k in range(N):
                if graph[j + k][i] != graph[N - 1 + j - k][i]:
                    break
                else: flag += 1
            if flag == N:
                count += 1
            flag = 0
    return count

for test_case in range(1, T + 1):
    N = int(input())
    graph = []
    for i in range(8):
        graph.append(input())
    ans = hori_check(graph, N) + verti_check(graph, N)
    print(f'#{test_case} {ans}')