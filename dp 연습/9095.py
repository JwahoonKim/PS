# An = An-1 + An-2 + An-3
T = int(input())
arr = [0] * T
for i in range(T):
    arr[i] = int(input())

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for x in range(4, max(arr) + 1):
    dp[x] = dp[x-1] + dp[x-2] + dp[x-3]

for i in range(T):
    print(dp[arr[i]])