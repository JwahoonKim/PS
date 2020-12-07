T = 10
for test_case in range(1, T + 1):
    N = int(input())
    h = list(map(int, input().split()))
    view = 0
    for i in range(2, N - 2):
        h_max = max(h[i - 2], h[i - 1], h[i + 1], h[i + 2])
        if h[i] - h_max > 0:
            view += h[i] - h_max
    print(f'#{test_case} {view}')