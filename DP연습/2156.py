import sys

n = int(input())
arr = [0]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
dp = [0] *(n + 1)

if n >= 1:
    dp[1] = arr[1]
if n >= 2:
    dp[2] = arr[1] + arr[2]
if n >= 3:
    for i in range(3, n + 1):
        way1 = dp[i - 1]
        way2 = dp[i - 3] + arr[i] + arr[i - 1]  
        way3 = dp[i - 2] + arr[i]
        dp[i] = max(way1, way2, way3)

print(dp[n])