n = int(input())
dp = [0] * (n + 2)
dp[1] = 1
dp[2] = 1
for i in range(n + 1):
    if i == 1 or i == 2:
        continue
    else :
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])
