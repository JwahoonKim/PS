from collections import deque

# 가장 중요도가 높은 문서인지 체크


def is_most_prior(arr, n):
    for idx, num in arr:
        if num > n:
            return False
    return True


n = int(input())

for _ in range(n):
    m, target_idx = map(int, input().split())
    arr = deque((enumerate(map(int, input().split()))))
    ans = 1
    while(1):
        now_idx, now_num = arr[0]
        if is_most_prior(arr, now_num):
            idx, num = arr.popleft()
            if idx == target_idx:
                print(ans)
                break
            else:
                ans += 1
        else:
            arr.append(arr.popleft())
