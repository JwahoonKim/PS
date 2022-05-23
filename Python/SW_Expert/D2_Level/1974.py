T = int(input())
def sdokuChecker(graph):
    checker = []
    oneToNine = [1,2,3,4,5,6,7,8,9]
    #1. 3 X 3 체크
    flag = [0, 3, 6]
    for k in flag:
        for n in flag:
            for i in range(3):
                for j in range(3):
                    checker.append(graph[k + i][n + j])
            checker.sort()
            if checker != oneToNine:
                    return 0
            checker = []
    #2. 가로 체크
    for i in range(9):
        for j in range(9):
            checker.append(graph[i][j])
        checker.sort()
        if checker != oneToNine:
            return 0
        checker = []
    #3. 세로 체크
    for i in range(9):
        for j in range(9):
            checker.append(graph[j][i])
            checker.sort()
        if checker != oneToNine:
            return 0
        checker = []
    return 1

for test_case in range(1, T + 1):
    sdoku = []
    for i in range(9):
        sdoku.append(list(map(int, input().split())))
    print(f'#{test_case} {sdokuChecker(sdoku)}')
    
