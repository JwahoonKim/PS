n = int(input())
dp = [[0,0,0]]

for i in range(1, n + 1):
    dp.append(list(map(int, input().split())))


for i in range(2, n + 1):
    dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] += min(dp[i - 1][2], dp[i - 1][0])
    dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])

R = dp[n][0] 
G = dp[n][1]
B = dp[n][2]

print(min(R,G,B))
