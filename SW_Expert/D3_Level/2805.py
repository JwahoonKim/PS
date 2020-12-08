T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    sum = 0
    center = N // 2
    left = center
    right = center
    for i in range(N):
        for j in range(left, right + 1):
            print(left, right)
            sum += int(graph[i][j])
        if i < center:
            left -= 1
            right += 1
        elif i >= center:
            left += 1
            right -= 1
    print(f'#{test_case} {sum}')



