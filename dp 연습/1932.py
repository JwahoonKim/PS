import sys
readline = sys.stdin.readline

n = int(input())
dp = [[0]]
for i in range(n):
    dp.append(list(map(int, readline().split())))

for i in range(2, n + 1):
    for j in range(i):
        if j == 0:
            dp[i][j] += dp[i - 1][j]
        elif j == i - 1:
            dp[i][j] += dp[i - 1][j - 1] 
        else :
            dp[i][j] += max(dp[i - 1][j-1], dp[i - 1][j])

ans = max(dp[n])
print(ans)