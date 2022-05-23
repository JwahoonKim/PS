T = 10
for test_case in range(1, T + 1):
    N = int(input())
    graph = []
    for i in range(100):
        graph.append(list(map(int, input().split())))
    sum_arr = []
    sum = 0 
    for i in range(100):
        # 가로
        for j in range(100):
            sum += graph[i][j]
        sum_arr.append(sum)
        sum = 0
        #세로
        for k in range(100):
            sum += graph[k][i]
        sum_arr.append(sum)
        sum = 0
    #오른쪽 아래 대각선
    for i in range(100):
        sum += graph[i][i]
    sum_arr.append(sum)
    sum = 0
    for i in range(100):
        sum += graph[i][99 - i]
    sum_arr.append(sum)
    ans = max(sum_arr)
    print(f'#{N} {ans}')