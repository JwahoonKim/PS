from itertools import combinations
T = int(input())
for test_case in range(1, T + 1):
    count = 0
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr2 = [i for i in arr if i <= k]
    for i in arr2:
        if k == i:
            count += 1
    for i in range(2, n + 1):
        arr3 = list(combinations(arr2, i))
        for i in arr3:
            if k == sum(i):
                count += 1
    print(f'#{test_case} {count}')
