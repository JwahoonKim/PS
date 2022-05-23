T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    pascal = [[0] * N for _ in range(N)]
    for i in range(N):
        pascal[i][0] , pascal[i][i] = 1, 1
    if N >= 3:
        for i in range(2, N):     
            for j in range(1, N - 1):
                pascal[i][j] = pascal[i - 1][j] + pascal[i - 1][j - 1]
    print(f'#{test_case}')
    for floor in pascal:
        for i in range(N):
            if floor[i] != 0:
                print(floor[i], end = " ")
        print("")

