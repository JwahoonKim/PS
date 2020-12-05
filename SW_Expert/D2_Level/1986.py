T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if i % 2 == 1:
            ans += i
        elif i % 2 == 0:
            ans -= i
    print(f'#{test_case} {ans}')
