import sys
readline = sys.stdin.readline

n = int(input())
arr = list(map(int, readline().split()))
dp = [0] * n

for i in range(n):
    if i == 0:
        dp[i] = arr[i]
    else:
        dp[i] = max(arr[i], arr[i] + dp[i - 1])

print(max(dp))
