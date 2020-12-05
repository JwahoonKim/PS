T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    max = 0
    sum = 0
    bug = []
    for i in range(N):
        bug.append(list(map(int, input().split())))
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            for k in range(M):
                for l in range(M):
                    sum += bug[i + k][j + l]
            if sum > max:
                max = sum
            sum = 0
    print(f'#{test_case} {max}')

