n = int(input())
day = [(0, 0)]
for _ in range(n):
    time, money = map(int, input().split())
    day.append((time, money))

# 돈은 n + 1일에 받는다고 취급
dp = [0] * (n + 2)

time = 0
money = 1

for i in range(1, n + 1):
    dp[i] = max(dp[: i + 1])
    if day[i][time] + i <= n + 1:
        future = i + day[i][time]
        dp[future] = max(dp[future], dp[i] + day[i][money])

print(max(dp))
